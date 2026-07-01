# Changelog

All notable changes to this project will be documented in this file.

## [0.3.0-candidate] - 2026-07-01

### Added

* Added `repair-policy.schema.json`.
* Added `repair-loop.schema.json`.
* Added `repair-record.schema.json`.
* Added `repair-policy.example.yaml`.
* Added `repair-loop.example.yaml`.
* Added `repair-record.example.yaml`.
* Updated `scripts/validate_examples.py` to validate v0.3 examples.
* Updated README with v0.3 repair loop documentation.

### Defined

* Repair Policy
* Repair Loop
* Repair Record
* Repair Trigger
* Repair Attempt
* Repair Action
* Repair Buffer
* Isolation Step
* Re-audit Step
* Final Repair Decision
* Repair Escalation
* Repair Safety Boundary

### Validation

* Confirmed that all v0.3 examples pass schema validation.
* Confirmed GitHub Actions validation passes successfully.

Validated v0.3 examples:

* `repair-policy.example.yaml`
* `repair-loop.example.yaml`
* `repair-record.example.yaml`

Full validation set:

* `replica-agent.example.yaml`
* `replica-breathing-cycle.example.yaml`
* `promotion-policy.example.yaml`
* `staging-policy.example.yaml`
* `exhalation-record.example.yaml`
* `retention-rule.example.yaml`
* `repair-policy.example.yaml`
* `repair-loop.example.yaml`
* `repair-record.example.yaml`

### Philosophy

v0.3 extends the breathing model by defining how the replica data center repairs flawed outputs.

v0.1 defined the basic breathing core.

v0.2 defined staging and exhalation.

v0.3 defines the repair immune layer:

* What triggers repair
* How flawed records are isolated
* What repair actions are allowed
* How many repair attempts are permitted
* When human review is required
* When risky records are quarantined
* When repeated failure leads to discard
* How repaired records are re-audited
* How final repair decisions are recorded

The goal is to prevent flawed replica outputs from silently entering the core data center.

### Core Flow

```text
Detect -> Isolate -> Repair -> Re-audit -> Reinstate or Discard
```

The repair loop complements the breathing flow:

```text
Inhale -> Stage -> Filter -> Compress -> Audit -> Exhale -> Retain or Promote
                                      |
                                      v
                              Detect -> Isolate -> Repair -> Re-audit
```

### Notes

This release establishes the repair loop layer for AI replica breathing infrastructure.

The protocol can now describe not only intake, staging, exhalation, and retention, but also controlled self-correction.

This makes the replica data center more resilient without allowing unlimited self-repair or unbounded agent behavior.

Future versions may extend the protocol with:

* Multi-replica coordination
* Energy-saving metrics
* Core memory promotion receipts
* Human review gates
* Replica orchestration receipts
* Cross-replica conflict resolution

## [0.2.0-candidate] - 2026-07-01

### Added

* Added `staging-policy.schema.json`.
* Added `exhalation-record.schema.json`.
* Added `retention-rule.schema.json`.
* Added `staging-policy.example.yaml`.
* Added `exhalation-record.example.yaml`.
* Added `retention-rule.example.yaml`.
* Updated `scripts/validate_examples.py` to validate v0.2 examples.
* Updated README with v0.2 staging and exhalation layer documentation.

### Defined

* Staging Policy
* Staging Zone
* Shadow Staging
* Candidate Pool
* Summary Cache
* Quarantine Zone
* Discard Buffer
* Exhalation Record
* Retention Rule
* Expiration Action
* Raw Input Handling
* Promotion Boundary

### Validation

* Confirmed that all v0.2 examples pass schema validation.
* Confirmed GitHub Actions validation passes successfully.

Validated v0.2 examples:

* `staging-policy.example.yaml`
* `exhalation-record.example.yaml`
* `retention-rule.example.yaml`

Full validation set:

* `replica-agent.example.yaml`
* `replica-breathing-cycle.example.yaml`
* `promotion-policy.example.yaml`
* `staging-policy.example.yaml`
* `exhalation-record.example.yaml`
* `retention-rule.example.yaml`

### Philosophy

v0.2 extends the breathing model by defining how the replica data center stages and exhales data.

v0.1 defined the basic breathing core.

v0.2 defines the lung valves:

* Where temporary data is placed
* How risky data is quarantined
* When raw data is compressed
* When temporary records expire
* What is discarded
* What is retained as a summary, hash, trace, or audit record
* What may be promoted to the core data center

The goal is to prevent AI replica infrastructure from becoming an uncontrolled storage dump.

### Core Flow

```text
Inhale -> Stage -> Filter -> Compress -> Audit -> Exhale -> Retain or Promote
```

### Notes

This release establishes the staging and exhalation layer for AI replica breathing infrastructure.

The protocol can now describe not only the existence of a breathing cycle, but also the concrete temporary zones, release actions, and retention rules that keep the replica layer lightweight.

Future versions may extend the protocol with:

* Replica repair loops
* Multi-replica coordination
* Energy-saving metrics
* Core memory promotion receipts
* Human review gates
* Replica orchestration receipts

## [0.1.0-candidate] - 2026-07-01

### Added

* Initial repository structure.
* Added `replica-agent.schema.json`.
* Added `replica-breathing-cycle.schema.json`.
* Added `promotion-policy.schema.json`.
* Added `replica-agent.example.yaml`.
* Added `replica-breathing-cycle.example.yaml`.
* Added `promotion-policy.example.yaml`.
* Added `scripts/validate_examples.py`.
* Added GitHub Actions validation workflow.
* Added `requirements.txt` for schema validation dependencies.

### Defined

* Replica Agent
* Breathing Cycle
* Staging Layer
* Filtering Layer
* Compression Layer
* Audit Layer
* Exhalation
* Promotion Policy
* Core Data Center promotion boundary

### Validation

* Confirmed that all v0.1 examples pass schema validation.
* Confirmed GitHub Actions validation passes successfully.

### Philosophy

v0.1 defines the minimum protocol for treating AI replica clusters as a breathing data center.

The replica layer receives, stages, filters, compresses, audits, exhales, and promotes data before it reaches the core data center.

The goal is not unlimited AI replication.

The goal is bounded, traceable, energy-efficient replica processing.

### Core Flow

```text
Inhale -> Stage -> Filter -> Compress -> Audit -> Exhale -> Promote
```

### Notes

This release establishes the first working protocol layer for AI replica breathing infrastructure.

Future versions may extend the protocol with:

* Staging and exhalation rules
* Retention policies
* Replica repair loops
* Multi-replica coordination
* Energy-saving metrics
* Core memory promotion receipts


