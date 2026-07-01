# Changelog

All notable changes to this project will be documented in this file.

## [0.5.0-candidate] - 2026-07-01

### Added

* Added `energy-budget-policy.schema.json`.
* Added `execution-metrics-record.schema.json`.
* Added `promotion-receipt.schema.json`.
* Added `energy-budget-policy.example.yaml`.
* Added `execution-metrics-record.example.yaml`.
* Added `promotion-receipt.example.yaml`.
* Updated `scripts/validate_examples.py` to validate v0.5 examples.
* Updated README with v0.5 energy budget and promotion receipt layer documentation.

### Defined

* Energy Budget Policy
* Budget Scope
* Token Budget
* Compute Budget
* Runtime Limit
* Core Model Activation Policy
* Energy Tracking Mode
* Execution Metrics Record
* Token Usage Record
* Runtime Record
* Energy Estimate
* Core Model Avoidance
* Estimated Savings Ratio
* Promotion Receipt
* Promotion Decision Basis
* Retained Artifacts
* Efficiency Summary
* Human Review Status
* Receipt Trace Requirement

### Validation

* Confirmed that all v0.5 examples pass schema validation.
* Confirmed GitHub Actions validation passes successfully.

Validated v0.5 examples:

* `energy-budget-policy.example.yaml`
* `execution-metrics-record.example.yaml`
* `promotion-receipt.example.yaml`

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
* `coordination-policy.example.yaml`
* `replica-handoff.example.yaml`
* `coordination-record.example.yaml`
* `energy-budget-policy.example.yaml`
* `execution-metrics-record.example.yaml`
* `promotion-receipt.example.yaml`

### Philosophy

v0.5 extends the breathing model by defining how the replica data center measures execution cost and proves core promotion.

v0.1 defined the basic breathing core.

v0.2 defined staging and exhalation.

v0.3 defined the repair immune layer.

v0.4 defined the coordination layer.

v0.5 defines the measurement and receipt layer:

* How many replicas may be active
* How many tokens may be used
* How long a task may run
* Whether the core model may be activated
* How execution metrics are recorded
* Whether the core model was avoided
* How many records were discarded or retained
* What estimated savings were achieved
* What was promoted to the core data center
* Why it was promoted
* Which artifacts were retained
* Whether human review approved the promotion
* Which trace and audit records are required

The goal is to make energy efficiency and core promotion auditable rather than merely aspirational.

### Core Flow

```text
Measure -> Budget -> Receipt -> Promote
```

The measurement and receipt loop complements the breathing, repair, and coordination flows:

```text
Inhale -> Stage -> Filter -> Compress -> Audit -> Exhale -> Retain or Promote
                                      |
                                      v
                              Detect -> Isolate -> Repair -> Re-audit
                                      |
                                      v
                              Assign -> Handoff -> Synchronize -> Resolve
                                      |
                                      v
                              Measure -> Budget -> Receipt -> Promote
```

### Notes

This release establishes the energy budget and promotion receipt layer for AI replica breathing infrastructure.

The protocol can now describe not only intake, staging, exhalation, retention, repair, and coordination, but also measurable execution cost and traceable promotion into the core data center.

This makes the replica data center more accountable as an energy-aware infrastructure layer.

Future versions may extend the protocol with:

* Human review gates
* Replica orchestration receipts
* Cross-replica conflict resolution
* Runtime budget enforcement profiles
* Local-first execution profiles
* Core memory promotion lifecycle
* External audit export formats

## [0.4.0-candidate] - 2026-07-01

### Added

* Added `coordination-policy.schema.json`.
* Added `replica-handoff.schema.json`.
* Added `coordination-record.schema.json`.
* Added `coordination-policy.example.yaml`.
* Added `replica-handoff.example.yaml`.
* Added `coordination-record.example.yaml`.
* Updated `scripts/validate_examples.py` to validate v0.4 examples.
* Updated README with v0.4 multi-replica coordination layer documentation.

### Defined

* Coordination Policy
* Coordination Mode
* Role Assignment
* Replica Handoff
* Handoff Receipt
* State Transfer
* Coordination Record
* Coordination Step
* Conflict Status
* Conflict Resolution Strategy
* Final Coordination State
* Multi-Replica Safety Boundary

### Validation

* Confirmed that all v0.4 examples pass schema validation.
* Confirmed GitHub Actions validation passes successfully.

Validated v0.4 examples:

* `coordination-policy.example.yaml`
* `replica-handoff.example.yaml`
* `coordination-record.example.yaml`

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
* `coordination-policy.example.yaml`
* `replica-handoff.example.yaml`
* `coordination-record.example.yaml`

### Philosophy

v0.4 extends the breathing model by defining how multiple replica agents coordinate safely.

v0.1 defined the basic breathing core.

v0.2 defined staging and exhalation.

v0.3 defined the repair immune layer.

v0.4 defines the coordination layer:

* How roles are assigned
* How many replicas may be active
* How work is handed off between replicas
* How handoff receipts are recorded
* How transferred state is bounded
* How conflicts are detected
* How conflicts are resolved
* When human review is required
* How final coordination state is recorded

The goal is to prevent AI replica infrastructure from becoming an unbounded swarm or a silent conflict generator.

### Core Flow

```text
Assign -> Handoff -> Synchronize -> Resolve -> Commit
```

The coordination loop complements the breathing and repair flows:

```text
Inhale -> Stage -> Filter -> Compress -> Audit -> Exhale -> Retain or Promote
                                      |
                                      v
                              Detect -> Isolate -> Repair -> Re-audit
                                      |
                                      v
                              Assign -> Handoff -> Synchronize -> Resolve
```

### Notes

This release establishes the multi-replica coordination layer for AI replica breathing infrastructure.

The protocol can now describe not only intake, staging, exhalation, retention, and repair, but also safe collaboration between multiple bounded replicas.

This makes the replica data center more capable as a coordinated cluster without allowing unlimited parallelism or uncontrolled self-replication.

Future versions may extend the protocol with:

* Energy-saving metrics
* Core memory promotion receipts
* Human review gates
* Replica orchestration receipts
* Cross-replica conflict resolution
* Runtime budget limits
* Local-first execution profiles

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


