# Validation

The source documentation reports end-to-end submission checks, owner-notification testing, and repairs to downstream flag writes. No raw execution logs or live checks were supplied for this portfolio.

| Proposed test | Acceptance condition |
|---|---|
| Form with multiple checkbox selections | One correctly mapped row and expected notice |
| Two submissions in the same second | Distinct IDs; historical format needs improvement |
| Multiple eligible rows in one poll | Each notification and flag update matches its source request |
| Second unchanged poll | No ordinary repeat notice |
| Slack succeeds; Excel flag update fails | Failure is detected and duplicate risk reconciled |
| Owner name not mapped | Visible actionable failure instead of silent omission |
| Owner reassigned | Defined re-notification behavior |
| Designer and PM paths paused | No messages or downstream side effects from those paths |
| Concurrent polls | No uncontrolled duplicate delivery |
| Invalid or unauthenticated submission | Rejected under the chosen access policy |

These are a proposed acceptance matrix, not newly passing tests. Measure submission completeness, unassigned backlog, time to owner assignment, duplicate messages, and failed-notification recovery before claiming business impact.
