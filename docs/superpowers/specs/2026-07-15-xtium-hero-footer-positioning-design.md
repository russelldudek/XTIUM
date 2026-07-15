# XTIUM Hero, Footer, and Transfer-Positioning Design

## Purpose

Repair three user-observed defects in the published XTIUM candidate vision:

1. the hero's overlapping operating plates obscure the causal relationship between internal proof and customer deployment;
2. the footer exposes the white background of the embedded official logo asset as an unexplained square;
3. the objection framing overemphasizes a career-path gap and reads more negatively than the evidence warrants.

The revision must preserve the campaign thesis: **Run it inside. Make it repeatable outside.**

## Approved Direction

Use a **Service Translation Spine** as the hero's signature visual.

The visual presents two clean operating states connected by one explicit translation mechanism:

- **Inside XTIUM — Operational proof**
- **For the customer — Deployment pattern**

Four aligned operating requirements create the complete causal model:

1. Promise
2. Authority
3. Evidence
4. Owner

Each internal definition must connect visibly to its customer-facing translation. The center is not a detached badge or obstruction; it is the mechanism that performs the translation.

## Hero Composition

### Desktop and laptop

The hero remains a two-column page composition:

- left: official XTIUM identity, relationship-target qualification, thesis, supporting copy, and actions;
- right: the Service Translation Spine.

The Service Translation Spine contains:

- a left column labeled `Inside XTIUM` with the subtitle `Operational proof`;
- a narrow center spine labeled `One Service Definition`;
- a right column labeled `For the customer` with the subtitle `Deployment pattern`;
- four horizontal rows connecting the same operating requirement across both states;
- visible teal-to-orange directional continuity from internal proof to customer deployment.

No cards may overlap. No absolute-positioned panel may obscure text. The mechanism must be understandable in a static screenshot.

### Tablet and mobile

The model stacks vertically in this order:

1. Inside XTIUM heading
2. internal operating definition
3. translation-spine label and directional cue
4. customer deployment definition

The four requirements remain grouped and aligned semantically. Mobile must not recreate overlap through transforms or negative margins.

## Motion

Motion explains translation rather than decorating cards.

On first view, the visual progresses through all four requirements in order:

`Promise -> Authority -> Evidence -> Owner`

For each row:

- the internal state receives a restrained teal emphasis;
- the center spine activates;
- the corresponding customer state receives an orange emphasis;
- the previous row returns to its resting state before the next row begins.

The full sequence must make every row relationship visible. It must not animate only one line or imply a partial operating system.

Under `prefers-reduced-motion: reduce`:

- no sequential animation runs;
- all four connections remain fully visible;
- no information depends on motion.

## Footer

Remove the official logo image from the dark footer. The current embedded raster source has a white background, and filtering it produces a visible white square.

The revised footer contains:

- a thin horizontal recognition rule using XTIUM teal and orange;
- `Independent candidate vision by Russell Dudek`;
- `AI Service Operations` as the neutral campaign descriptor;
- verified location, phone, email, and LinkedIn details;
- no logo image, pseudo-logo, monogram, or empty visual block.

The official XTIUM identity remains visible above the fold in the navigation and hero, satisfying employer-recognition requirements without duplicating the mark in a technically unsafe context.

## Positive Transfer Positioning

Replace the current objection panel and heading with a positive transfer case.

### Heading

`Why the experience transfers`

### Approved copy

Russell's career has not followed the conventional global-MSP path—and that is precisely where the transfer value sits.

He has built operating mechanisms across 24/7 customer operations, technical delivery, high-reliability environments, service and support workflows, and AI-enabled transformation. Across those settings, the recurring work has been the same: making complexity visible, clarifying ownership and escalation, establishing repeatable operating practices, and connecting technology investments to measurable customer outcomes.

That outside-in operating perspective can help XTIUM accelerate integration, strengthen service consistency, and convert internal AI progress into customer-ready managed-service capabilities. A focused operating conversation would quickly identify where that experience could create the greatest immediate leverage.

### Tone constraints

- Do not disguise that Russell lacks conventional global-MSP tenure.
- Do not frame that fact as the dominant recruiter-facing message.
- Do not use `gap`, `objection`, `not equivalent`, `bounded diagnostic`, or defensive disclaimer language in the visible panel.
- Lead with relevant operating capability and explain the value of outside-in transfer.

## Accessibility and Interaction Requirements

- Preserve semantic headings and reading order.
- The translation visual must remain understandable without animation.
- Decorative connection elements use `aria-hidden="true"`.
- Text contrast must meet WCAG AA.
- The visual may not create horizontal scrolling at 390, 768, 1280, or 1440 pixel widths.
- Focus behavior and existing hero actions remain unchanged.
- The existing interactive service-scenario artifact below the hero remains the page's meaningful participation mechanism.

## Files in Scope

- `index.html`: replace hero visual markup, replace transfer-positioning panel copy and heading, remove footer logo markup.
- `styles.css`: replace overlapping plate/register rules with translation-spine rules; add responsive and reduced-motion behavior; revise footer treatment; update positive-transfer panel styling if needed.
- `app.js`: add only the minimal hero-sequence state logic required for the four-row translation animation; preserve existing scenario tabs and menu behavior.
- `scripts/publication_qa.py`: add source-level assertions that reject the old overlapping plate structure, require the translation-spine structure, require the positive heading, and reject footer images.
- `.github/workflows/live-verification.yml`: update computed-style and interaction assertions to target the new hero structure rather than `.plate`.
- `.github/workflows/deploy-and-audit.yml`: update live visual assertions to target the new hero structure rather than `.plate`.

## Verification Contract

Before publication, verify:

1. `index.html`, `styles.css`, `app.js`, logo, routes, and PDFs remain present on `main`.
2. The old `.register`, `.plate`, `.plate.left`, `.plate.right`, and `.registration-mark` hero markup/rules are removed.
3. The hero contains all four translation rows and both operating-state labels.
4. The footer contains no `<img>` element.
5. The visible evidence panel heading is `Why the experience transfers`.
6. The old negative copy is absent.
7. Chromium renders the live page at 1440x900, 1280x800, 768x1024, and 390x844 with:
   - applied CSS;
   - no horizontal overflow;
   - no console or page errors;
   - a legible static translation model;
   - all four row relationships visible;
   - no footer white square.
8. Reduced-motion rendering exposes the complete model and uses no active transition or animation duration.
9. Existing service-scenario tabs, mobile menu, document routes, links, and PDF downloads still work.
10. Candidate-facing confidentiality and exact PDF page-count checks remain passing.

## Scope Boundary

This change does not revise the campaign thesis, research, resume, cover letter, interview brief, 120-day plan, service-definition canvas, or broader information architecture. It is a focused correction to the hero's causal visual integrity, footer rendering, and transfer-positioning tone.
