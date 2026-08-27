# Nexus Model & Simulation Card

## System
Nexus is a hybrid agent-based simulation combining deterministic economic/social rules with optional LLM-mediated citizen cognition.

## Intended use
Research, education, scenario exploration, and experimentation around heterogeneous agents and coupled social/economic systems.

## Not intended for
Real-world financial, political, cybersecurity, employment, or policy decisions. Outputs are synthetic and assumption- and seed-dependent.

## Agent design
Citizens have heterogeneous wealth, skills, risk tolerance, education, preferences, relationships, goals, memories, employment and portfolios. LLMs may propose bounded actions; deterministic validators enforce constraints.

## Limitations
- The world model is stylized and does not reproduce a real country.
- Economic and social rates are simplified.
- LLM cognition can vary by provider/model/version.
- Synthetic markets are not forecasts.
- Real-world calibration is not claimed until explicitly demonstrated.

## Evaluation
Releases should report deterministic seed tests, invariants, multi-seed replication, sensitivity analysis, runtime scaling, and LLM/provider metadata.

## Safety
Cybersecurity is modeled as abstract incidents and resilience outcomes. No exploit payloads or operational intrusion instructions are part of the simulator.
