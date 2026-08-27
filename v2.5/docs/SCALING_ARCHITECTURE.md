# Nexus v2.5 Scaling Architecture

- `SimulationWorker` owns live-world mutation and serializes tick jobs.
- LLM cognition uses bounded parallel batches for network-bound providers.
- WebGL2 can render population-density overlays while Canvas retains detailed sprites.
- SQLite persists experiment metadata/results and checkpoints in the current prototype.
- For 10k+ agents, the production path is multi-process simulation shards + Redis/NATS event bus + PostgreSQL/TimescaleDB.

The research model should remain deterministic at the world-state level even when visualization and network-bound cognition are asynchronous.
