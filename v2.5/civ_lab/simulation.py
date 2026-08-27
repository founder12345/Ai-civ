"""
Nexus v2.5 deterministic simulation orchestrator.

The LLM may propose actions, but deterministic subsystems validate and apply
state changes. The fixed tick order keeps experiments reproducible.
"""
from __future__ import annotations
import random
from .models import Citizen, Company, WorldState, Party
from . import economy, society, politics, events as events_module, city
from .llm import LLMClient, create_llm_client, ResilientLLMClient
from . import cognition, advanced, cybersecurity, research_plus, global_layer
from .performance import PerformanceGovernor

class Simulation:
    def __init__(self, seed: int = 42, llm: LLMClient | None = None):
        self.rng = random.Random(seed)
        self.citizens: dict[int, Citizen] = {}
        self.companies: dict[int, Company] = {}
        self.parties: dict[int, Party] = politics.seed_parties()
        self.world = WorldState()
        self._next_citizen_id = 1
        self.city_layout: city.CityLayout | None = None
        self.llm: LLMClient = llm or create_llm_client()
        global_layer.initialize(self.world, self.rng)
        self.performance = PerformanceGovernor()

    def _allocate_citizen_id(self) -> int:
        self._next_citizen_id = max(self._next_citizen_id, max(self.citizens, default=0) + 1)
        new_id = self._next_citizen_id
        self._next_citizen_id += 1
        return new_id

    def step(self, n: int = 1) -> None:
        for _ in range(n):
            started = self.performance.begin()
            profile = self.performance.profile(self.world.population or len(self.citizens))
            self.world.performance_cognition_cap = profile.recommended_cognition_cap
            self.world.replay_stride = profile.replay_stride
            self.world.tick += 1
            economy.tick(self.citizens, self.companies, self.world, self.rng, layout=self.city_layout)
            society.tick(self.citizens, self.companies, self.world, self.rng, self._allocate_citizen_id)
            politics.tick(self.citizens, self.parties, self.world, self.rng)
            cognition.run_cognition_pass(self.citizens, self.companies, self.world, self.llm, layout=self.city_layout, rng=self.rng, parties=self.parties)
            advanced.tick_finance(self.citizens, self.companies, self.world, self.rng)
            research_plus.tick_banking(self.citizens, self.companies, self.world, self.rng)
            research_plus.tick_information(self.citizens, self.world, self.rng)
            research_plus.tick_learning(self.citizens, self.world)
            advanced.tick_government(self.citizens, self.companies, self.world, self.rng)
            advanced.tick_society_network(self.citizens, self.world, self.rng)
            advanced.tick_generations(self.citizens, self.companies, self.world, self.rng, self._allocate_citizen_id)
            advanced.tick_environment_and_technology(self.citizens, self.companies, self.world, self.rng)
            cybersecurity.tick(self.citizens, self.companies, self.world, self.rng)
            advanced.tick_international(self.world, self.rng)
            global_layer.tick(self.world, self.companies, self.rng)
            advanced.record_macro(self.world)
            if self.world.tick % max(1, self.world.replay_stride) == 0:
                self.world.replay_history.append({"tick": self.world.tick, "stats": self.stats()})
                self.world.replay_history[:] = self.world.replay_history[-self.performance.max_replay_points:]
            self.performance.end(started)
            city.tick(self.citizens, self.companies, self.world, self.city_layout, self.rng)

    def llm_status(self) -> dict:
        client = self.llm
        primary = client.primary if isinstance(client, ResilientLLMClient) else client
        provider = getattr(primary, "provider_name", type(primary).__name__)
        model = getattr(primary, "model", "deterministic")
        is_mock = type(primary).__name__ == "MockLLMClient"
        return {"mode": "mock" if is_mock else "real", "provider": provider, "model": model,
                "fallback": bool(getattr(client, "failed_over", False)), "last_error": getattr(client, "last_error", None),
                "calls_today": self.world.llm_calls_today, "calls_total": self.world.llm_calls_total,
                "daily_limit": self.world.max_cognitions_per_day}

    def apply_sandbox_variable(self, path: str, value) -> str:
        parts = path.split(".")
        scope = parts[0]
        if scope == "world":
            field = parts[1]
            if not hasattr(self.world, field): raise ValueError(f"Unknown world field: {field}")
            setattr(self.world, field, value); msg = f"SANDBOX: world.{field} set to {value}"
        elif scope == "company":
            company_id, field = int(parts[1]), parts[2]
            company = self.companies[company_id]
            if not hasattr(company, field): raise ValueError(f"Unknown company field: {field}")
            setattr(company, field, value); msg = f"SANDBOX: company {company.name}.{field} set to {value}"
        elif scope == "citizen":
            citizen_id, field = int(parts[1]), parts[2]
            citizen = self.citizens[citizen_id]
            if not hasattr(citizen, field): raise ValueError(f"Unknown citizen field: {field}")
            setattr(citizen, field, value); msg = f"SANDBOX: citizen {citizen.name}.{field} set to {value}"
        else: raise ValueError(f"Unknown sandbox scope: {scope}")
        self.world.log(msg); return msg

    def trigger_event(self, event_name: str, severity: float = 0.5) -> str:
        return events_module.trigger_event(self.world, self.citizens, event_name, severity, self.rng, self.companies)

    def stats(self) -> dict:
        w = self.world
        ruling_party = self.parties.get(w.ruling_party_id) if w.ruling_party_id else None
        return {"tick": w.tick, "gdp": round(w.gdp, 2), "unemployment_rate": round(w.unemployment_rate, 4),
                "inflation": round(w.inflation, 4), "interest_rate": w.interest_rate, "tax_rate": w.tax_rate,
                "avg_happiness": round(w.avg_happiness, 3), "avg_wealth": round(w.avg_wealth, 2),
                "gini_estimate": round(w.gini_estimate, 3), "crime_rate": round(w.crime_rate, 3),
                "government_budget": round(w.government_budget, 2), "government_approval": round(w.government_approval, 3),
                "ruling_party": ruling_party.name if ruling_party else None, "population": w.population,
                "births_total": w.births_total, "deaths_total": w.deaths_total, "marriages_total": w.marriages_total,
                "active_companies": sum(1 for c in self.companies.values() if not c.is_bankrupt),
                "bankrupt_companies": sum(1 for c in self.companies.values() if c.is_bankrupt),
                "active_events": {name: eff["severity"] for name, eff in w.active_event_effects.items()},
                "llm_calls_total": w.llm_calls_total, "llm_calls_today": w.llm_calls_today,
                "max_cognitions_per_day": w.max_cognitions_per_day, "llm_input_tokens_total": w.llm_input_tokens_total,
                "llm_output_tokens_total": w.llm_output_tokens_total, "llm_estimated_cost_usd": round(w.llm_estimated_cost_usd, 4),
                "tier2_decisions_total": w.tier2_decisions_total, "llm_mode": self.llm_status()["mode"],
                "llm_provider": self.llm_status()["provider"], "llm_model": self.llm_status()["model"],
                "llm_fallback": self.llm_status()["fallback"], "housing_price_index": round(w.housing_price_index, 2),
                "stock_market_index": round(w.stock_market_index, 2),
                "market_cap": round(sum(co.stock_price * co.shares_outstanding for co in self.companies.values() if not co.is_bankrupt), 2),
                "investing_citizens": sum(1 for book in w.portfolios.values() if any(float(v) > 0 for v in book.values())),
                "poverty_rate": round(w.poverty_rate, 4), "polarization": round(w.polarization, 4),
                "social_cohesion": round(w.social_cohesion, 4), "productivity_index": round(w.productivity_index, 2),
                "trade_balance": round(w.trade_balance, 2), "exchange_rate": round(w.exchange_rate, 4),
                "energy_price": round(w.energy_price, 3), "government_debt": round(w.government_debt, 2),
                "infrastructure": round(w.infrastructure, 3), "environmental_quality": round(w.environmental_quality, 3),
                "technology_progress": round(w.technology_progress, 3), "cybersecurity": cybersecurity.stats(w)}
