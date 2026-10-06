# Operating procedure

## Before a controlled demo

Use synthetic records in a separate workbook. Check endpoint configuration, credentials, tool references, tracker columns, and workflow availability. Verify a single request end to end before presenting. Do not expose the historical unauthenticated POC for public submissions or concurrent users.

## Normal flow

Submit intake, complete the chat, then independently inspect the exact record ID in the tracker. Verify status and every operational field. Completion means requirement capture only. Operations staff remain responsible for approvals and provisioning.

## Troubleshooting

| Symptom | Check | Action |
|---|---|---|
| Confirmation fails | Redirect endpoint and query encoding | Correct demo configuration |
| Chat does not open | Widget initialization and chat endpoint | Inspect browser error and endpoint response |
| Wrong or missing context | Metadata, exact record lookup, session binding | Stop the demo; do not use the latest row as a substitute |
| Save appears successful but row is unchanged | Save execution and tracker response | Treat as incomplete; correct failure and reconcile the exact row |
| Raw JSON in reply | Prompt and output handling | Restore presentation rules and retest |

## Change control

Pause new sessions and drain in-flight work before structural changes. Export a secure private backup, edit in a test environment, run the validation matrix, then publish. Roll back to the last tested version on failure and reconcile partially written records. Keep role guidance in prompt and lookup tool consistent.
