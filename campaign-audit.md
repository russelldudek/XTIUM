# Campaign Audit

Campaign state: building — live publication verification pending

## User-steering revision delta

Observed defect: The public campaign appeared unstyled.

Why the prior audit missed it: Local artifacts were inspected, but the complete public `main` manifest was not re-fetched before handoff. The public repository contained neither `index.html` nor `styles.css`, so no live page could load the intended visual system.

Rejected execution: A local ZIP and partial repository staging were treated as an adequate handoff. They were not.

Approved correction: Publish the complete campaign as one atomic Git tree containing every HTML route, stylesheet, script, brand asset, document, and PDF. Verify `index.html`, `styles.css`, `brand-tokens.css`, and all linked assets directly from `main` before any completion claim.

Affected routes and artifacts: All six HTML routes, shared CSS, JavaScript, official XTIUM identity asset, five PDFs, README, source record, and campaign audit.

Regression coverage added: `scripts/publication_qa.py` now fails on a missing stylesheet, missing CSS token file, broken internal asset, root-absolute deployment path, incorrect PDF page count, missing candidate-vision URL, incomplete manifest, or public confidentiality violation.

Verification evidence: Local publication QA passes. Public `main` and live-route verification must pass after the atomic tree commit.

## Current local checks

- Complete source manifest: passed
- Shared stylesheet chain: passed
- Internal HTML, image, script, and PDF paths: passed
- Resume PDF: exactly 2 pages
- Relationship letter PDF: exactly 1 page
- Interview brief PDF: exactly 3 pages
- 120-day plan PDF: exactly 2 pages
- Service Definition Canvas PDF: exactly 1 page
- Candidate-facing confidentiality source scan: zero matches
- Reduced-motion source treatment: present
- Keyboard interaction source treatment: present

The campaign may not be classified complete until the committed `main` manifest and the live GitHub Pages routes are independently verified.
