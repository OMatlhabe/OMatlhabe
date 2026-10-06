# Maintaining this portfolio

For each material change:

1. Update the affected project README, design, SOP, and decision log together.
2. Identify whether the change is implemented, reported historically, proposed, or independently verified.
3. Use synthetic records and generic recipient mappings only.
4. Inspect every new screenshot for names, tabs, account information, URLs, IDs, and execution payloads.
5. Run `python3 scripts/check_portfolio.py` before publishing.
6. Record the change and validation in CHANGELOG.md. Prefer a branch and pull request for subsequent changes.

Review the roadmap and evidence status monthly and after material project changes. Add metrics only with a defensible baseline, measurement period, and attribution. Keep private exports and backups outside this repository.

Future JSON exports need a recursive review of credentials, parameters, code, prompts, pinned data, static data, cached links, metadata, resource IDs, and embedded HTML. Import them inactive into an isolated demo environment, reconnect only demo credentials, and run the acceptance matrix before labelling them reusable.
