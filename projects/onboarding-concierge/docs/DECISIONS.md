# Decisions and debugging

| Issue or choice | Documented response | Lesson or remaining gap |
|---|---|---|
| chatInput lost during context enrichment | Rebuilt the merge around the original payload | Preserve trigger fields; protect them from accidental overwrite |
| Record metadata missing from redirect | Added record ID to URL and widget metadata | Verify every integration boundary |
| Stale or malformed model-supplied record ID | Added exact matching and a latest-pending fallback | The fallback is unsafe under concurrency; identity must be server-controlled |
| Agent exposed raw JSON or unresolved syntax | Clarified presentation instructions | Prompting helps presentation, but does not replace output validation |
| Embedded widget storage failure | Added Map-backed in-memory storage before widget load | Test actual browser context and reload behavior |
| Small role catalogue | Chose readable guidance and keyword lookup over RAG | Add retrieval complexity only when the data warrants it |
| Model choice | Retested Haiku after inlining guidance | No benchmark supports a numerical cost or speed claim |

## Proposed improvements

Remove cross-record fallback first. Add authentication and request binding, deterministic validation, save-result acknowledgements, and error alerts. Then add an evaluation dataset for unknown roles, injection attempts, missing fields, long conversations, and persistence failures.
