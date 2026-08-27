# NEXUS — Autonomous Civilization Research Platform

> **A reproducible agent-based simulation for studying how autonomous citizens, markets, institutions, information and crises interact.**

[![Research](https://img.shields.io/badge/status-research--release-blue)](#research-status) [![Reproducible](https://img.shields.io/badge/reproducibility-seeded%20experiments-success)](#reproducibility) [![Python](https://img.shields.io/badge/python-3.11%2B-informational)](#quick-start)

## 🌍 What is Nexus?

Nexus is a synthetic civilization laboratory. Citizens have needs, goals, memory, beliefs and bounded perception; they move through a living city, work, consume, save, invest and interact. Companies, banks, markets, government, information networks, technology and cybersecurity co-evolve with the population.

The goal is **not** to claim that the simulated agents are conscious or that Nexus predicts the real economy. The goal is to create a controlled environment where hypotheses about complex adaptive systems can be made explicit, tested repeatedly and reproduced from seeds.

### Core systems

- 🧠 Autonomous citizen cognition and persistent memory
- 🚶 Need-driven, path-based citizen movement
- 💵 USD-denominated household, business and banking economics
- 📈 Financial markets and local business investment
- 🏦 Credit, banking and crisis propagation
- 🏛️ Politics, institutions and collective behavior
- 🗣️ Social information and cultural evolution
- 🤖 Provider-agnostic LLM cognition with deterministic fallback
- 🛡️ Cybersecurity events and bounded system response
- 🔬 Experiment runner, sensitivity analysis and ablations
- ♻️ Deterministic seeds, fingerprints and reproduction tooling
- 🧯 Checkpoints, supervision and graceful recovery
- ⚡ Worker-based simulation and performance telemetry
- 🎮 Living-city visualization with smooth movement and ambient systems

## 🔬 Research status

**Research Release 1.0 / model v2.5.** The project is research-ready as a synthetic modeling platform, but it is **not yet a validated real-world forecasting model**. Historical comparison, calibration and independent replication are explicitly tracked as research work rather than hidden behind a marketing claim.

See [`v2.5/docs/RESEARCH_STATUS_V2.5.md`](v2.5/docs/RESEARCH_STATUS_V2.5.md), [`v2.5/docs/MODEL_CARD.md`](v2.5/docs/MODEL_CARD.md) and [`v2.5/docs/VALIDATION.md`](v2.5/docs/VALIDATION.md).

## 🧪 Reproducible research

The repository includes experiment manifests, seeds, results, analysis code and a clean-room reproduction script. Research artifacts are separated from the interactive application so experiments can be rerun without relying on the UI or an external LLM provider.

```text
research/
├── PAPER.md
├── DATA_SOURCES.md
├── RESEARCH_RELEASE.md
├── REPLICATION_REQUEST.md
├── experiment_manifest.json
├── reproduce.py
└── results_table.csv
```

> **Important:** results produced by an earlier model version are historical artifacts. Any model change requires a fresh research campaign.

## 🏗️ Architecture

```text
                    ┌──────────────────────────┐
                    │       NEXUS WORLD         │
                    └────────────┬─────────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          ▼                      ▼                      ▼
      Citizens               Economy              Institutions
          │                      │                      │
      cognition              markets                politics
      memory                 banking               culture
      goals                  housing                information
          └──────────────────────┼──────────────────────┘
                                 ▼
                         World consequences
                                 │
                         memory + learning
                                 ↺
```

The v2.5 hardened engine adds a supervisor, checkpoints and bounded recovery around the deterministic simulation core. See [`v2.5/docs/FAILURE_MODES.md`](v2.5/docs/FAILURE_MODES.md) and [`v2.5/docs/SCALING_ARCHITECTURE.md`](v2.5/docs/SCALING_ARCHITECTURE.md).

## 🤖 Free AI setup

The recommended zero-cost local configuration is **Ollama + Qwen3**. Nexus treats an LLM as a proposal generator: the deterministic simulation validates and applies actions, so an LLM failure cannot directly corrupt the world state.

See [`FREE_LLM_SETUP.md`](FREE_LLM_SETUP.md).

## 🚀 Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python run_simulation.py
```

API:

```bash
python api.py
```

Then open `city.html` for the interactive city or `dashboard.html` for the research dashboard.

## 🧪 Tests

```bash
python critical_test.py
python -m compileall -q .
```

GitHub Actions runs the core checks automatically.

## ☁️ Deployment

- Frontend configuration: [`vercel.json`](vercel.json)
- Backend configuration: [`render.yaml`](render.yaml)
- Lovable can use the repository as the source for the browser application while the simulation/API runs as a separate service.

## 📚 Research documents

| Document | Purpose |
|---|---|
| [`research/PAPER.md`](research/PAPER.md) | Research narrative and results |
| [`research/RESEARCH_RELEASE.md`](research/RESEARCH_RELEASE.md) | Release-level research record |
| [`research/DATA_SOURCES.md`](research/DATA_SOURCES.md) | External reference datasets |
| [`research/REPLICATION_REQUEST.md`](research/REPLICATION_REQUEST.md) | Independent replication request |
| [`v2.5/docs/MODEL_CARD.md`](v2.5/docs/MODEL_CARD.md) | Model scope and limitations |
| [`v2.5/docs/VALIDATION.md`](v2.5/docs/VALIDATION.md) | Validation protocol |
| [`v2.5/docs/FAILURE_MODES.md`](v2.5/docs/FAILURE_MODES.md) | Failure and recovery design |
| [`v2.5/docs/SCALING_ARCHITECTURE.md`](v2.5/docs/SCALING_ARCHITECTURE.md) | Scaling strategy |

## ⚠️ Scientific boundaries

Nexus is a **simulation**, not a claim of artificial general intelligence or machine consciousness. Its cognition layer provides persistent state, goals, memory, planning and LLM-assisted decisions; these are computational constructs and should not be interpreted as evidence of subjective experience.

Likewise, a successful simulation experiment does not establish that the same causal effect exists in the real world. Real-world claims require calibration, external validation and independent replication.

## 📌 Roadmap

- [ ] Complete post-v2.5 calibration campaign
- [ ] Expand long-horizon / large-population experiments
- [ ] Publish full raw experiment bundles and figures
- [ ] Independent external replication
- [ ] Benchmark alternative agent architectures
- [ ] Add stronger historical calibration where data support it

## License

See repository licensing and attribution files before redistributing Nexus or its research artifacts.
