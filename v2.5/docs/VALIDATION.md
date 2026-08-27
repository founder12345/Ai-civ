# Nexus Validation Plan

A serious Nexus result requires more than code execution.

1. Software verification — compilation, regression tests, API checks and deterministic hashes.
2. Invariants — population, wealth, portfolios, prices, debt and bounded variables remain valid.
3. Behavioral validation — interventions move relevant metrics without hard-coded outcomes.
4. Sensitivity — vary assumptions and measure robustness.
5. Stochastic replication — independent seeds and confidence intervals.
6. Ablation — compare major subsystems enabled versus disabled.
7. Calibration — claim real-world validity only after fitting to an explicit dataset and reporting the procedure.
8. External review — publish code, manifests, seeds, outputs and methodology.

## Research Assistant

Evaluate groundedness, uncertainty, structured output, deterministic fallback and read-only behavior.

Endpoint: `POST /assistant/ask`.
