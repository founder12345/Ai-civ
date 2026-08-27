# Nexus v2.5 — Research Status and Corrections

This release fixes issues identified during the v1.0 research audit. Previous empirical results are retained as historical artifacts but are superseded where mechanisms changed.

## Corrections

1. Scheduled interventions now stop exactly at the intervention tick.
2. Interest rates now transmit through firm investment capacity and hiring thresholds.
3. Technology breakthroughs propagate through firm technology/productivity and the aggregate productivity index.
4. Automation can displace a bounded number of workers so employment effects are measurable.
5. Bank failure includes a bounded depositor haircut plus partial government backstop.
6. Benchmarks use population-aware horizons to avoid CI/free-tier timeouts.
7. Experiment snapshots explicitly record interest rate and productivity.

## Verification

- Python compilation: PASS
- Core regression suite: PASS
- Critical cognition suite: PASS
- Performance benchmark: PASS at 50/100/500/1000 agents
- Exact intervention scheduling: PASS

## Scientific status

v1.0 empirical results must not be presented as validation of v2.5. Publications using v2.5 should rerun the full hypothesis, sensitivity, ablation and historical-validation suite from fresh seeds. Nexus remains a synthetic research platform, not a calibrated forecasting model. External human replication remains open.
