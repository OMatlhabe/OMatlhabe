# Design

## Requirements

One intake point captures request type, submitter, title, description, expected outcome, relevant contacts, broad audience and geography, links, learning requirements, target dates, success criteria, and optional sponsorship. Exact organization-specific audience lists and internal programme names are omitted.

Checkbox arrays are flattened to comma-separated tracker values. Creation metadata and notification flags are set by the workflow, not trusted from form input.

## Tracker model

| Group | Fields |
|---|---|
| Request context | Form inputs described above |
| Lifecycle | Request ID, created timestamp, creator, status, health indicator, reporting period |
| Assignment | Enablement owner, designer, project manager |
| Notification state | Owner Notified, Closure Notified, ID Notified, PM Notified |

Status and health are different concepts: a request can be In Progress and at risk. Reporting-period rules should be configurable rather than copied from an internal fiscal calendar.

## Limits and discrepancies

The original request ID uses a timestamp to second precision. It is sortable, but simultaneous submissions can collide. A robust reconstruction should add a random suffix or UUID and enforce uniqueness.

The source reports 19 fields but lists 18. The exact original schema is unverified without an export. Source claims about authentication are also insufficient to establish that the form endpoint itself was protected. Verify access controls separately from credential authentication.
