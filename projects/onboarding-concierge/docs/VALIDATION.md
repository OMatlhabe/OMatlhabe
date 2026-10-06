# Validation

## Historical evidence

The supplied decision log reports four end-to-end conversations, coverage of sales, engineering, marketing, and finance role paths, and a Haiku retest after prompt changes. These are documented historical checks; no live tests were run during portfolio preparation and raw execution evidence is absent.

## Proposed acceptance tests

| Scenario | Required result | Status |
|---|---|---|
| Known role completes | Same request row updated; all required fields captured | Reported historically; not independently rerun |
| Two overlapping requests | No context or write crosses between records | Not verified; known fallback risk |
| Missing or tampered record ID | Reject lookup/write; request recovery | Proposed |
| Unknown role | Explicit uncertainty and clarification | Proposed |
| Tracker write fails | No success claim; alert and recoverable state | Proposed |
| Untrusted chat asks to alter another record | Server validation rejects action | Proposed |
| Reload or long conversation | Predictable recovery without losing identity | Proposed |

Measure completion rate, manual correction rate, wrong-record writes, failed-save detection, latency, and cost per completed request before making production or ROI claims.
