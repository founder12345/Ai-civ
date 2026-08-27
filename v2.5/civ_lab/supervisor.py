"""Nexus engine supervisor: locking, health, checkpoints and graceful recovery."""
from __future__ import annotations
import threading, time
from dataclasses import dataclass

@dataclass
class EngineHealth:
    status: str = "starting"
    last_tick_ms: float = 0.0
    consecutive_failures: int = 0
    total_recoveries: int = 0
    last_error: str | None = None
    last_checkpoint_tick: int = 0
    tick_count: int = 0

class EngineSupervisor:
    def __init__(self, checkpoint_store, checkpoint_every: int = 50, recovery_factory=None):
        self.lock = threading.RLock()
        self.checkpoint_store = checkpoint_store
        self.checkpoint_every = checkpoint_every
        self.health = EngineHealth()
        self._last_checkpoint = 0
        self.recovery_factory = recovery_factory

    def run(self, sim, steps: int = 1):
        steps = max(1, min(int(steps), 500))
        with self.lock:
            started = time.perf_counter()
            try:
                sim.step(steps)
                elapsed = (time.perf_counter() - started) * 1000
                self.health.status = "healthy"
                self.health.last_tick_ms = round(elapsed, 2)
                self.health.consecutive_failures = 0
                self.health.last_error = None
                self.health.tick_count += steps
                if sim.world.tick - self._last_checkpoint >= self.checkpoint_every:
                    try:
                        self.checkpoint_store.save(sim, f"auto-{sim.world.tick}")
                        self.checkpoint_store.save(sim, "previous")
                        self.checkpoint_store.save(sim, "latest")
                    except Exception as checkpoint_exc:
                        self.health.last_error = f"checkpoint warning: {type(checkpoint_exc).__name__}: {checkpoint_exc}"
                    self._last_checkpoint = sim.world.tick
                    self.health.last_checkpoint_tick = sim.world.tick
                return {"recovered": False, "elapsed_ms": round(elapsed, 2)}
            except Exception as exc:
                self.health.status = "recovering"
                self.health.consecutive_failures += 1
                self.health.last_error = f"{type(exc).__name__}: {exc}"
                try:
                    loaded = False
                    for checkpoint_id in ("latest", "previous"):
                        try:
                            self.checkpoint_store.load(sim, checkpoint_id)
                            loaded = True
                            break
                        except Exception:
                            continue
                    if not loaded:
                        raise RuntimeError("no valid recovery checkpoint available")
                    self.health.total_recoveries += 1
                    self.health.status = "recovered"
                    self.health.consecutive_failures = 0
                    self._last_checkpoint = sim.world.tick
                    self.health.last_checkpoint_tick = sim.world.tick
                    return {"recovered": True, "elapsed_ms": round((time.perf_counter()-started)*1000, 2)}
                except Exception as recovery_exc:
                    if self.recovery_factory is not None:
                        try:
                            fresh = self.recovery_factory()
                            sim.__dict__.clear(); sim.__dict__.update(fresh.__dict__)
                            self.health.total_recoveries += 1
                            self.health.status = "recovered_reset"
                            self.health.consecutive_failures = 0
                            self._last_checkpoint = sim.world.tick
                            self.health.last_checkpoint_tick = sim.world.tick
                            self.health.last_error = f"{self.health.last_error}; checkpoint recovery failed, clean world restored"
                            return {"recovered": True, "full_reset": True, "elapsed_ms": round((time.perf_counter()-started)*1000, 2)}
                        except Exception as reset_exc:
                            recovery_exc = reset_exc
                    self.health.status = "failed"
                    self.health.last_error = f"{self.health.last_error}; recovery failed: {type(recovery_exc).__name__}: {recovery_exc}"
                    return {"recovered": False, "failed": True, "elapsed_ms": round((time.perf_counter()-started)*1000, 2)}

    def snapshot(self, sim):
        with self.lock:
            return {"status": self.health.status, "tick": sim.world.tick, "population": sim.world.population,
                    "last_tick_ms": self.health.last_tick_ms, "consecutive_failures": self.health.consecutive_failures,
                    "total_recoveries": self.health.total_recoveries, "last_checkpoint_tick": self.health.last_checkpoint_tick,
                    "last_error": self.health.last_error, "checkpoint_interval": self.checkpoint_every,
                    "engine_generation": getattr(sim.world, "engine_generation", 0),
                    "replay_points": len(getattr(sim.world, "replay_history", []))}

class SimulationWorker:
    """Single-owner simulation worker; HTTP requests submit work instead of mutating state directly."""
    def __init__(self, supervisor, sim):
        import queue
        self.supervisor = supervisor; self.sim = sim; self._queue = queue.Queue()
        self._thread = threading.Thread(target=self._loop, name="nexus-sim-worker", daemon=True); self._thread.start()

    def _loop(self):
        while True:
            fn, event, box = self._queue.get()
            try: box["value"] = fn()
            except BaseException as exc: box["error"] = exc
            finally: event.set()

    def submit(self, fn, timeout=120):
        event = threading.Event(); box = {}
        self._queue.put((fn, event, box))
        if not event.wait(timeout): raise TimeoutError("simulation worker timed out")
        if "error" in box: raise box["error"]
        return box.get("value")

    def step(self, steps=1): return self.submit(lambda: self.supervisor.run(self.sim, steps))
    def replace_sim(self, sim): return self.submit(lambda: self._replace(sim))
    def _replace(self, sim): self.sim = sim; return True
    def health(self):
        return {"alive": self._thread.is_alive(), "queue_depth": self._queue.qsize(), "thread": self._thread.name}
