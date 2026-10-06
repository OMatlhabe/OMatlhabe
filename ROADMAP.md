# Roadmap

## Priority 1: correctness and evidence

- Concierge: eliminate latest-pending fallback; enforce authenticated record/session binding.
- Concierge: validate save inputs and require confirmed persistence before a success response.
- Intake: reconcile the original form schema and validate paused-branch behavior from execution evidence.
- Intake: replace second-resolution IDs with collision-resistant identifiers.

## Priority 2: recoverability

- Add explicit error alerts and reconciliation procedures.
- Replace silent recipient lookup failures with observable outcomes.
- Define assignment-change notification behavior and prevent overlapping delivery attempts.

## Priority 3: reusable demonstration

- Obtain and sanitize original exports only if publication rights allow.
- Build separate inactive demo exports using synthetic data and independent credentials.
- Run concurrency, partial failure, invalid input, and role-coverage tests.
- Capture measured completion, correction, delivery, latency, and cost data.

All items are proposed. No completion is implied by inclusion here.
