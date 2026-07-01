# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0-candidate] - 2026-07-01

### Added

- Initial repository structure.
- Added `replica-agent.schema.json`.
- Added `replica-breathing-cycle.schema.json`.
- Added `promotion-policy.schema.json`.
- Added minimal YAML examples.
- Added validation script for schema/example consistency.
- Added GitHub Actions workflow for validation.

### Defined

- Replica Agent
- Breathing Cycle
- Staging Layer
- Exhalation
- Promotion Policy
- Core Data Center promotion boundary

### Philosophy

v0.1 defines the minimum protocol for treating AI replica clusters as a breathing data center.

The replica layer receives, stages, filters, compresses, audits, discards, and promotes data before it reaches the core data center.
requirements.txt
jsonschema>=4.22.0
PyYAML>=6.0.1
