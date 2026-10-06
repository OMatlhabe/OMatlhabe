# Implementation guide

No importable JSON is included. This guide describes the system without internal configuration.

1. Create a synthetic request table and define input fields, assignments, status, and notification flags.
2. Build form to append to new-request notification. Flatten checkbox arrays, map creator correctly, and generate collision-resistant IDs in a reconstruction.
3. Validate tracker dropdowns and health formatting against the form definitions.
4. Add a scheduled table read and independent filters for closure, owner, designer, and project-manager events.
5. Preserve item lineage through filtered Code-node output. Each retained item must point to its actual input index; downstream updates must resolve the correct request ID.
6. Send a notification, then update its matching flag only after success. Test partial failures and reconcile duplicates rather than assuming transactional delivery.
7. Use synthetic recipient mappings in development. Verify mapping failures produce an actionable signal.
8. Keep designer and project-manager notifications paused until rollout criteria are met. Verify they send no messages in actual executions.
9. Test with multiple eligible rows, mixed notification flags, and a second polling cycle.

Bind Microsoft 365 and Slack credentials only in the environment. Do not place tokens, channel/user IDs, workbook IDs, tenant URLs, or internal recipient maps in public files.

For historical imports, use a controlled path that shares the validation and append logic. Decide whether notifications are desired and throttle explicitly. Remove temporary import triggers after verification.
