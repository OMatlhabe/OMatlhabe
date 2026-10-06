# Implementation guide

This is a generalized reconstruction guide, not an import-ready export. No original JSON is supplied.

1. Create a synthetic tracker with the schema in DESIGN.md and a named Excel table.
2. Build intake, generate a server-side record ID, append a pending row, and prepare the redirect metadata.
3. Build role lookup and record persistence independently. Test each with synthetic inputs before attaching the agent.
4. Build chat context resolution and preserve chatInput while enriching the payload. Bind record identity outside the model and reject unknown or ambiguous IDs.
5. Attach a model, scoped memory, and the two tools. Keep role guidance editable; require confirmation before saving.
6. Build the confirmation page. Configure its chat endpoint with a placeholder until a demo endpoint exists. Pass metadata consistently and verify storage behavior.
7. Test the whole chain with two simultaneous synthetic requests, then a failed tracker write. Do not claim completion until persistence reports success.

## Configuration

Use independently provisioned least-privilege Microsoft 365 and model credentials. Rebind workbook/table references, tool workflow references, redirect endpoint, and chat endpoint in your own environment. No internal webhook, credential, or tenant IDs belong in this repository.

Historical POC behavior is documented in DECISIONS.md. The safe record-binding requirements here are proposed corrections, not claims that the original workflow already implements them.
