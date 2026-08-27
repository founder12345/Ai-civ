# Nexus

> **An autonomous-agent civilization laboratory** — simulate minds, markets, institutions, crises, and societies; then run reproducible experiments on them.

[![Research Status](https://img.shields.io/badge/research-v2.5%20hardened-blue)](RESEARCH_STATUS_V2.5.md) [![Reproducibility](https://img.shields.io/badge/reproducibility-seeded-green)](reproduce.py) [![License](https://img.shields.io/badge/license-MIT-black)](LICENSE)

## Why Nexus?

Nexus is a research-oriented agent-based simulation in which citizens have persistent internal state, needs, beliefs, memory, goals and plans, while the surrounding civilization contains firms, housing, banking, financial markets, politics, information, cybersecurity and technological change.

The core design principle is **LLM proposals + deterministic world validation**: an LLM can suggest a decision, but it cannot directly mutate the simulated world.

## Research questions

Nexus is built to investigate questions such as:

- How do autonomous agents react to monetary tightening?
- How do financial shocks propagate through households and firms?
- What happens when automation changes productivity and labor demand?
- How do information, social learning and institutions alter collective outcomes?
- Which mechanisms generate inequality, housing cycles and systemic risk?

## Current research release

**v2.5 Research Hardened** is the current model freeze for scientific evaluation. Earlier research results are explicitly superseded where the underlying mechanisms changed.

The repository includes:

- 🧠 Autonomous-agent cognition and persistent memory
- 💵 USD-denominated economic system
- 🏦 Banking, credit, equities and financial contagion
- 🏠 Housing and employment
- 🗳️ Politics and institutions
- 🛡️ Cybersecurity events
- 🌐 Information and social dynamics
- 🔬 Experiment runner, seeds, ablations and sensitivity analysis
- 📈 Publication-quality figures and raw experiment outputs
- ♻️ Checkpointing, supervisor and recovery architecture
- ⚡ Performance/scaling benchmarks
- 🤖 Free-first local LLM setup with Ollama/Qwen

## Repository map

```text
src/                 Core simulator, API and interactive city
├── civ_lab/         Agents, cognition, economy, markets, society, research
├── city.html        Living-city visualization
├── dashboard.html   Research/observability dashboard
├── api.py           Flask API
└── test_suite.py    Regression tests

Research artifacts
├── PAPER.md
├── Nexus_Research_Paper_v1.0.pdf
├── experiment_manifest.json
├── hypothesis_summary.json
├── raw_H*.json
├── ablation_*.json
├── sensitivity_*.json
├── historical_us_reference.json
└── *.png

Research documentation
├── MODEL_CARD.md
├── VALIDATION.md
├── RESEARCH_STATUS_V2.5.md
├── RESEARCH_RELEASE.md
├── RESEARCH_PLATFORM.md
├── AGENT_MIND_SPEC.md
├── ARCHITECTURE.md
└── SCALING_ARCHITECTURE.md
```

## Run locally

```bash
cd src
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python critical_test.py
python api.py
```

Open `city.html` for the interactive civilization.

### Free local AI

Install Ollama and a compatible local model (Qwen recommended). See [`src/FREE_LLM_SETUP.md`](src/FREE_LLM_SETUP.md).

## Reproduce the research

The research artifacts are designed around explicit seeds and manifests.

```bash
python reproduce.py
```

See [`REPLICATION_REQUEST.md`](REPLICATION_REQUEST.md) for an independent-reproduction protocol.

## Scientific status

Nexus is a **research-ready synthetic modeling platform**, not a validated forecasting model and not a claim of artificial consciousness or AGI. Historical comparisons are directional unless explicitly calibrated and validated. Failed hypotheses and model limitations are retained rather than hidden.

## Citation

See [`src/CITATION.cff`](src/CITATION.cff).

## Contributing

Issues and independent replications are welcome. If you reproduce a result, please report the commit, environment, seeds, and exact command used.

## License

MIT. See [`LICENSE`](LICENSE).
