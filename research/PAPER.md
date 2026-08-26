# Nexus: A Reproducible Autonomous-Agent Civilization Simulation

## Abstract
Nexus is an agent-based civilization simulation combining autonomous citizens, economic institutions, financial markets, information dynamics, politics, cybersecurity, and an interactive research layer. This release evaluates the model using 1,250 seeded simulation runs across five explicit hypotheses, component ablations, parameter sensitivity analysis, a U.S. macroeconomic reference comparison, and a deterministic reproduction check.

The results show several robust internal responses, including a large negative stock-market response to a bank-failure intervention, a large housing-price response to monetary tightening, and poverty reduction under universal basic income. Other expected responses fail to appear, including unemployment responses to monetary tightening and automation. A technology intervention increases GDP without changing the explicit productivity metric. These failures are treated as model-development findings, not hidden results.

Nexus should therefore be described as a research-ready synthetic agent-based modeling platform, not a validated forecasting model.

## Design
Five hypotheses were tested with paired control/treatment simulations using identical deterministic seeds. Each core run used 30 citizens, 6 companies and 360 ticks (15 simulated days), with deterministic/mock cognition. The core ensemble contains 500 paired experiments, or 1,000 simulation runs. Additional ablation, sensitivity, baseline and pandemic-validation runs bring the total to 1,250.

## Main results
- H1 Monetary tightening: housing prices fell strongly, but unemployment did not respond.
- H2 Universal basic income: poverty fell and happiness rose slightly; GDP also rose.
- H3 AI automation: the expected unemployment increase did not appear.
- H4 Bank failure: stock-market stress was large and negative, but household wealth moved slightly upward.
- H5 Technology breakthrough: GDP rose strongly, while the explicit productivity metric did not move.

## Historical comparison
U.S. reference data are used only for directional validation. BEA reports real GDP changes of -2.1% in 2020, 6.2% in 2021, 2.5% in 2022, 2.9% in 2023 and 2.8% in 2024. BLS reports annual unemployment of 8.1%, 5.3%, 3.6%, 3.6% and 4.0%. BLS annual CPI inflation was 1.2%, 4.7%, 8.0%, 3.8% and 2.9%. The Nexus pandemic benchmark did not reliably reproduce the joint GDP/unemployment response.

## Limitations
Parameters are synthetic; the population and horizon are small; financial, banking and productivity mechanisms are simplified; LLM cognition is excluded from causal claims; and historical comparison is directional rather than calibration. Automated reproduction is not independent human replication.
