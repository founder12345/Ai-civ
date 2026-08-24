# Nexus — AI Civilization Simulation

Nexus is an agent-based civilization simulator where citizens, companies, markets, politics, housing, technology, society and crises interact in a deterministic simulation.

## Highlights

- Citizen cognition with provider-agnostic LLM support
- Free-first AI: local Ollama/Qwen3, OpenRouter free routing, Anthropic, then safe mock fallback
- Endogenous economy, businesses, employment, housing, credit and equities
- Politics, elections, social networks, generations and environmental dynamics
- Experiment mode with deterministic seeds and fingerprints
- SQLite checkpoints and restore
- Flask API + browser dashboards
- Vercel frontend and Render backend deployment configs

## Quick start

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python run_simulation.py
```

Open `city.html` or serve the project with a static server. For the API:

```bash
python api.py
```

## Free AI

The recommended zero-cost local setup is Ollama with Qwen3. See [FREE_LLM_SETUP.md](FREE_LLM_SETUP.md).

Nexus never lets an LLM directly mutate the world. The model proposes an action; the deterministic simulation validates and applies it.

## Deployment

- Frontend: Vercel using `vercel.json`
- Simulation/API: Render using `render.yaml`

The Render service intentionally uses one worker because the live simulation state is held in process memory. Threads provide concurrent HTTP handling without splitting the world into disconnected worker processes.

## Testing

```bash
python critical_test.py
python -m compileall -q .
```

GitHub Actions runs both checks automatically.

## Project layout

```text
.
├── api.py
├── run_simulation.py
├── critical_test.py
├── city.html
├── dashboard.html
├── civ_lab/
│   ├── actions.py
│   ├── advanced.py
│   ├── city.py
│   ├── cognition.py
│   ├── economy.py
│   ├── events.py
│   ├── experiment.py
│   ├── llm.py
│   ├── memory.py
│   ├── models.py
│   ├── persistence.py
│   ├── politics.py
│   ├── seed.py
│   ├── simulation.py
│   └── society.py
├── .github/workflows/test.yml
├── render.yaml
└── vercel.json
```

## Status

Nexus v1.0 is feature-complete for the current architecture. The next improvements should be product polish, richer visualization, real-world model evaluation, and production scaling rather than adding disconnected mechanics.
