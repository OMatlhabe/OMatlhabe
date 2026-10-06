# Decisions and iterations

| Problem | Documented response | Engineering lesson |
|---|---|---|
| Repeat-notification risk | Reduced notification scope, fixed state updates, then rebuilt branches | Stabilize the core before extending it |
| Missing pairedItem lineage | Linked retained filter output to source input indices | Multi-item tests expose mapping failures that single-row tests miss |
| Stale removed-field reference | Removed the stale mapping and verified the flag write | Schema changes need a consumer audit |
| Incorrect creator mapping | Used the actual submitter field | Similar field names do not imply equivalent meaning |
| Imported rows bypassed notifications | Reused the submission append/notify chain individually | Share business logic instead of duplicating it |
| Source and tracker counts differed | Traced an existing genuine request separately | Reconcile by identity, not row position or count alone |
| Row deletion unavailable in the configured connector | Used authorized spreadsheet UI operations | Connector constraints should shape the operating procedure |
| Generic credential reuse was blocked | Respected the security boundary | Do not bypass administrative restrictions |
| Assignment roles were not ready | Kept designer and PM notifications paused | Separate technical capability from operational rollout |

Internal names, source records, channel configuration, and browser-session details are excluded. Proposed collision handling, durable notification delivery, and recipient-key improvements are future work, not retrospective implementation claims.
