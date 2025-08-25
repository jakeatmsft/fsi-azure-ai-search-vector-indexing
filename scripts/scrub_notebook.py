import json
import sys
from pathlib import Path

def scrub_ipynb(path: Path) -> bool:
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return False
    if not isinstance(data, dict) or 'cells' not in data:
        return False

    changed = False
    for cell in data.get('cells', []):
        if cell.get('cell_type') == 'code':
            if cell.get('outputs'):
                cell['outputs'] = []
                changed = True
            if 'execution_count' in cell and cell['execution_count'] is not None:
                cell['execution_count'] = None
                changed = True
    if changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    return changed

def main():
    root = Path('.')
    total = 0
    for p in root.rglob('*.ipynb'):
        # Skip hidden and .git directories
        if any(part.startswith('.') for part in p.parts):
            continue
        if scrub_ipynb(p):
            total += 1
    print(f'Scrubbed {total} notebooks')

if __name__ == '__main__':
    sys.exit(main())