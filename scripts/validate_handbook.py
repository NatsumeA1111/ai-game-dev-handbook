"""Offline structural checks, not game QA or skill behavior verification."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
for path in root.rglob("*.md"):
    if ".git" in path.parts:
        continue
    text = path.read_text()
    for target in re.findall(r"\[[^\]]*\]\(([^ )]+)(?: +[^)]*)?\)", text):
        if ":" in target or target.startswith("#"):
            continue
        file = target.split("#", 1)[0]
        if file and not (path.parent / file).exists():
            errors.append(f"{path.relative_to(root)}: missing {file}")
for path in (root / ".agents/skills").glob("*/SKILL.md"):
    text = path.read_text()
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        errors.append(f"{path}: missing frontmatter")
        continue
    fields = dict(re.findall(r"^(name|description): (.+)$", parts[1], re.M))
    if fields.get("name") != path.parent.name or not re.fullmatch(r"[a-z0-9-]{1,63}", fields.get("name", "")):
        errors.append(f"{path}: invalid name")
    if not fields.get("description"):
        errors.append(f"{path}: missing description")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("PASS: local Markdown file links and simple skill name/description frontmatter")
print("Not checked: remote URLs, anchor IDs, arbitrary YAML, game behavior or skill efficacy")
