# Operating procedure

## Intake and triage

Requestors submit a clear description, desired outcome, audience, dates, and success criteria. Operations staff review the tracker row from the notification, set an accountable owner, and progress status as work begins. The tracker remains the authoritative queue.

## Routine checks

Check recent submissions against tracker rows and notifications. Inspect scheduled executions for errors and unresolved recipient mappings. Reconcile sent messages whose flag update failed before resetting flags or retrying. Review stale requests and identity mappings regularly.

Terminal status should trigger a closure notice on a later scheduled cycle; owner assignment should trigger an owner notice. Polling introduces delay and failures can extend it. Do not promise instant updates.

## Reassignment and rollout

The documented design requires a manual flag reset to notify a reassigned owner. Verify the intended recipient before resetting. Before enabling designer or PM notifications, audit existing eligible rows, mappings, and historical flags to avoid a burst of old notices. Test in a controlled environment first.

## Troubleshooting

| Symptom | Check |
|---|---|
| No row | Form mapping, table configuration, credential access |
| Row exists but no immediate notice | Slack execution and destination configuration |
| Owner never receives notice | Exact recipient mapping, eligibility and flag state |
| Repeated notices | Send/mark partial failure, item lineage, overlapping executions |
| Wrong row marked | Request ID uniqueness and source item pairing |

Back up privately before changes, pause affected execution paths, test the validation matrix, and restore the previous tested configuration on failure. Reconcile partially completed work. Keep form options and tracker validation synchronized. No internal execution payloads belong in public issues.
