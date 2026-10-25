"""Check publication text and local Markdown targets. Images require human review."""
from pathlib import Path
import os, re, sys
ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    'UUID or webhook identifier': r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b',
    'Slack identity': r'(?-i:\b[CUW](?=[A-Z0-9]*[0-9])[A-Z0-9]{8,}\b)' ,
    'token-shaped value': r'(?:xox[baprs]-[A-Za-z0-9-]+|sk-ant-[A-Za-z0-9_-]+|gh[pousr]_[A-Za-z0-9_]+)',
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    'live integration URL': r'https?://[^\s)]+(?:sharepoint\.com|/webhook/|/webhook-test/)[^\s)]*',
}
# Supply private organization terms, names and identifiers at scan time;
# never commit them into a public checker.
private_terms = [v.strip() for v in os.environ.get('PORTFOLIO_PRIVATE_TERMS', '').split(',') if v.strip()]
if private_terms:
    PATTERNS['private reference'] = '|'.join(re.escape(v) for v in private_terms)
errors = []
files = [p for p in ROOT.rglob('*') if p.is_file() and p.suffix in {'.md','.json','.yml','.yaml','.csv','.html'}]
for path in files:
    content = path.read_text()
    for label, pattern in PATTERNS.items():
        if re.search(pattern, content, re.I):
            errors.append(f'{path.relative_to(ROOT)}: {label}')
    if path.suffix == '.md':
        for target in re.findall(r'\]\(([^\s)]+)', content):
            if target.startswith(('https://','http://','mailto:','#')):
                continue
            target = target.split('#')[0]
            if not (path.parent / target).exists():
                errors.append(f'{path.relative_to(ROOT)}: missing target {target}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'PASS: {len(files)} text files checked; local Markdown links resolve. Images need visual review.')
