# Free AI setup

Nexus supports a free-first cognition chain:

1. **Ollama + Qwen3** (recommended local option)
2. **OpenRouter free routing** (cloud option, rate-limited)
3. Anthropic if configured
4. Mock fallback so the simulation never depends on an external model

## Ollama

Install Ollama, then:

```bash
ollama pull qwen3:8b
```

Configure:

```env
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://127.0.0.1:11434/v1
OLLAMA_MODEL=qwen3:8b
```

## OpenRouter

Set:

```env
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=your_key
OPENROUTER_MODEL=openrouter/free
```

Free routing is quota/rate limited and model availability can change.

## Safety architecture

The LLM never mutates simulation state directly. It returns a structured proposal; Nexus validates the proposal against the simulation rules before applying it.

Never commit `.env` or API keys. Use `.env.example` as the template.
