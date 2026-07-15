from __future__ import annotations

import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = [
    "index.html",
    "resume.html",
    "cover-letter.html",
    "interview-brief.html",
    "120-day-plan.html",
    "service-definition-canvas.html",
]
PDF_PAGES = {
    "docs/Russell-Dudek-XTIUM-Resume.pdf": 2,
    "docs/Russell-Dudek-XTIUM-Relationship-Letter.pdf": 1,
    "docs/Russell-Dudek-XTIUM-Interview-Brief.pdf": 3,
    "docs/Russell-Dudek-XTIUM-120-Day-Plan.pdf": 2,
    "docs/XTIUM-AI-Enabled-Service-Definition-Canvas.pdf": 1,
}
REQUIRED = [
    *HTML_FILES,
    "styles.css",
    "brand-tokens.css",
    "app.js",
    "brand-intelligence.md",
    "sources.md",
    "README.md",
    "campaign-audit.md",
    "assets/brand/xtium-logo.svg",
    *PDF_PAGES,
]
FORBIDDEN = re.compile(r"role[\s_-]*forge", re.IGNORECASE)
ATTR_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']")


def fail(message: str) -> None:
    raise AssertionError(message)


def resolve_internal(source: Path, raw: str) -> Path | None:
    parsed = urlparse(raw)
    if parsed.scheme or raw.startswith(("#", "mailto:", "tel:", "javascript:")):
        return None
    if raw.startswith("/"):
        fail(f"Root-absolute path is not GitHub Pages safe: {source.name}: {raw}")
    path = raw.split("#", 1)[0].split("?", 1)[0]
    if not path:
        return None
    return (source.parent / path).resolve()


def pdf_pages(path: Path) -> int:
    result = subprocess.run(
        ["pdfinfo", str(path)], check=True, capture_output=True, text=True
    )
    match = re.search(r"^Pages:\s+(\d+)$", result.stdout, re.MULTILINE)
    if not match:
        fail(f"Could not determine PDF page count: {path}")
    return int(match.group(1))


def main() -> None:
    for rel in REQUIRED:
        path = ROOT / rel
        if not path.is_file() or path.stat().st_size == 0:
            fail(f"Missing or empty required artifact: {rel}")

    styles = (ROOT / "styles.css").read_text(encoding="utf-8")
    tokens = (ROOT / "brand-tokens.css").read_text(encoding="utf-8")
    if '@import url("brand-tokens.css")' not in styles:
        fail("styles.css must import brand-tokens.css")
    if styles.count("{") != styles.count("}"):
        fail("styles.css has unbalanced braces")
    for token in ("--xtium-ink", "--xtium-teal", "--xtium-orange", "--campaign-signal"):
        if token not in tokens:
            fail(f"Missing CSS custom property: {token}")

    for rel in HTML_FILES:
        source = ROOT / rel
        text = source.read_text(encoding="utf-8")
        if 'rel="stylesheet" href="styles.css"' not in text:
            fail(f"Stylesheet link missing from {rel}")
        if 'src="app.js"' not in text:
            fail(f"Application script missing from {rel}")
        for raw in ATTR_RE.findall(text):
            target = resolve_internal(source, raw)
            if target is not None and not target.exists():
                fail(f"Broken internal asset from {rel}: {raw}")

    for rel, expected in PDF_PAGES.items():
        actual = pdf_pages(ROOT / rel)
        if actual != expected:
            fail(f"{rel}: expected {expected} pages, found {actual}")

    for rel in ("resume.html", "cover-letter.html"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        if "https://russelldudek.github.io/XTIUM/" not in text:
            fail(f"Visible candidate-vision URL missing from {rel}")

    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() not in {".pdf"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            if FORBIDDEN.search(text) or FORBIDDEN.search(str(path.relative_to(ROOT))):
                fail(f"Forbidden internal process name found in {path.relative_to(ROOT)}")

    print("Publication QA passed: complete manifest, CSS chain, internal assets, PDFs, links, and confidentiality checks.")


if __name__ == "__main__":
    main()
