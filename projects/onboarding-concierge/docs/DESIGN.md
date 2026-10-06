# Design and data model

## Scope

A hiring manager submits identity and scheduling information, then confirms equipment, software, access, training, and exceptions through chat. Operations staff act on the completed record. The agent gathers requirements; it does not authorize or provision access.

## Requirements

- Six visible intake fields: manager, new hire, role, team, location, start date.
- One authoritative server-generated record ID passed throughout the workflow chain.
- One question per turn; reuse existing context instead of asking for it again.
- Plain-language closing summary following a successful save.
- Role guidance editable without an embedding pipeline.

## Record schema

| Group | Fields | Writer |
|---|---|---|
| Identity | Record ID, timestamp, manager, new hire, role, team, location, start date | Intake |
| State | Pending Consultation; Complete | Intake; save tool |
| Requirements | Work mode, equipment, software, system access, first training module, special requirements, summary | Save tool |

The public examples use invented identities. The original workbook name and configuration are omitted.

## Boundaries

This POC has no approvals, SLA management, authentication, or access provisioning. Keyword categories are coarse. Scanning the whole tracker limits scale. Completion indicates requirements were captured, not that onboarding has been fulfilled.

The original timestamp-plus-random identifier format is not an authorization mechanism. Production requires an authenticated session bound to an authorized record and deterministic server-side validation of tool inputs.
