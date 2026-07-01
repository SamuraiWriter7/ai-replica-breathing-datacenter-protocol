# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0-candidate] - 2026-07-01

### Added

- Initial repository structure.
- Added `replica-agent.schema.json`.
- Added `replica-breathing-cycle.schema.json`.
- Added `promotion-policy.schema.json`.
- Added `replica-agent.example.yaml`.
- Added `replica-breathing-cycle.example.yaml`.
- Added `promotion-policy.example.yaml`.
- Added `scripts/validate_examples.py`.
- Added GitHub Actions validation workflow.
- Added `requirements.txt` for schema validation dependencies.

### Defined

- Replica Agent
- Breathing Cycle
- Staging Layer
- Filtering Layer
- Compression Layer
- Audit Layer
- Exhalation
- Promotion Policy
- Core Data Center promotion boundary

### Validation

- Confirmed that all v0.1 examples pass schema validation.
- Confirmed GitHub Actions validation passes successfully.

### Philosophy

v0.1 defines the minimum protocol for treating AI replica clusters as a breathing data center.

The replica layer receives, stages, filters, compresses, audits, exhales, and promotes data before it reaches the core data center.

The goal is not unlimited AI replication.

The goal is bounded, traceable, energy-efficient replica processing.

### Core Flow

```text
Inhale -> Stage -> Filter -> Compress -> Audit -> Exhale -> Promote
Notes

This release establishes the first working protocol layer for AI replica breathing infrastructure.

Future versions may extend the protocol with:

Staging and exhalation rules
Retention policies
Replica repair loops
Multi-replica coordination
Energy-saving metrics
Core memory promotion receipts
