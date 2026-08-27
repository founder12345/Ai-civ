# Nexus v2.5 — Research Hardened

This directory contains the current research-hardened simulator release. It is intentionally separated from legacy material so the public repository preserves model lineage.

## Core modules

- `civ_lab/simulation.py` — deterministic orchestration and subsystem ordering
- `civ_lab/supervisor.py` — single-owner worker, checkpointing and recovery
- `civ_lab/cognition.py` — autonomous-agent cognition
- `civ_lab/economy.py` — USD economy, firms, employment and policy transmission
- `civ_lab/advanced.py` — finance, technology, institutions and global systems
- `civ_lab/research_plus.py` — banking, information and learning
- `civ_lab/experiment.py` — reproducible experiments
- `civ_lab/llm.py` — provider abstraction and safe fallbacks

## Research artifacts

The root `research/` directory contains experiment manifests, results, reproduction tooling and research documentation. v2.5 supersedes earlier model results where mechanisms changed.

## Scientific status

Nexus is a research-ready synthetic modeling platform. It is not a validated forecasting model and does not claim artificial consciousness or AGI. Claims should be made only from reproducible experiments with explicit seeds and manifests.
