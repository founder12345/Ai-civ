# Nexus Failure Modes & Safeguards

| Failure | Safeguard |
|---|---|
| Simulation exception | Supervisor checkpoint recovery + clean reset fallback |
| Concurrent tick requests | Single-owner simulation worker |
| Bad checkpoint | Latest/previous fallback |
| LLM outage | Deterministic cognition fallback |
| LLM request storm | Bounded batch concurrency |
| Browser render exception | Frame-level recovery |
| Oversized API payload | Request-size limit |
| API abuse | Rate limiting |
| Short experiment misses event | Exact intervention-tick scheduler |
| Long benchmark timeout | Population-aware benchmark horizon |
| Nondeterministic provider in causal study | Deterministic mock cognition |

No software is literally uncrashable. Production deployment should additionally use durable external checkpoints, managed databases, process supervision, observability and backups.
