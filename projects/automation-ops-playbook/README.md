# Automation Operations Playbook

**Author:** Oratile Matlhabe · **Type:** Reusable agent skill · **Status:** Portfolio edition; runtime validation required for each workflow.

An automation can complete a test run and still leave its owner with missed records, duplicate messages or unnoticed failures. This skill provides a repeatable way to scope, review and maintain recurring automations.

## What it demonstrates

- Operational discovery: trigger, data contract, owner, intended outcome and failure behaviour.
- Quality assurance: branch coverage, duplicates, item lineage, concurrency and partial failure.
- Reliability: bounded retries, reconciliation, rollback and recovery verification.
- Ownership: monitoring of business outcomes, credential continuity and inventory maintenance.
- Evidence-based release decisions that distinguish inspection from executed tests.

## Use it

Read [SKILL.md](SKILL.md), or place it in an `automation-ops-playbook` folder in your agent's documented skills directory. Custom-skill import support varies by product; it does not grant access to your automation platform.

Example prompt: “Review this n8n workflow before release. Here is the export and a redacted execution trace. Identify gaps, propose tests, and state what has actually been verified.”

The skill selects build intake, release review, or takeover/maintenance from context. It produces a check register, unresolved actions and a scoped readiness decision. See the [fictional review example](examples/example-review.md).

## Boundaries

This is an instruction-based review tool, not an automated test runner or monitoring service. It needs workflow evidence and authorized runtime tests. No production adoption, measured improvement or universal reliability guarantee is claimed. See [validation and limitations](VALIDATION.md).

The [Handover SOP Builder](../handover-sop-builder/README.md) complements this project by documenting how another person operates and maintains the resulting process.

## Licence

No licence grant is included for this playbook in this edition. The uploaded MIT licence accompanied the SOP Builder package; it has not been extended to this separate project without the author's choice.
