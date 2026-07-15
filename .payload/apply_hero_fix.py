from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
index_path = root / "index.html"
styles_path = root / "styles.css"

html = index_path.read_text(encoding="utf-8")
css = styles_path.read_text(encoding="utf-8")

html = html.replace(
    'class="register ready" id="registration" aria-label="Two aligned operating plates: internal XTIUM run and customer deployment run"',
    'class="register translation-spine ready" id="registration" aria-label="Service Translation Spine showing how operational proof inside XTIUM becomes a customer deployment pattern through one service definition"',
    1,
)
html = html.replace(
    '<h2>Adjacent evidence, honestly applied.</h2></div><p>The transfer case is operating-mechanism depth across 24/7 customer operations, AI-enabled service and support workflows, high-reliability technology, standard work and post-launch learning.</p>',
    '<h2>Operating depth that travels.</h2></div><p>The transfer case is built on operating-mechanism depth across 24/7 customer operations, AI-enabled service and support workflows, high-reliability technology, standard work and post-launch learning.</p>',
    1,
)

transfer_case = (
    '<aside class="transfer-case"><p class="kicker">Transfer advantage</p>'
    '<h3>Why the experience transfers</h3>'
    '<p><strong>Russell\'s career has not followed the conventional global-MSP path—and that is precisely where the transfer value sits.</strong></p>'
    '<p>He has built operating mechanisms across 24/7 customer operations, technical delivery, high-reliability environments, service and support workflows, and AI-enabled transformation. Across those settings, the recurring work has been the same: making complexity visible, clarifying ownership and escalation, establishing repeatable operating practices, and connecting technology investments to measurable customer outcomes.</p>'
    '<p>That outside-in operating perspective can help XTIUM accelerate integration, strengthen service consistency, and convert internal AI progress into customer-ready managed-service capabilities. A focused operating conversation would quickly identify where that experience could create the greatest immediate leverage.</p>'
    '</aside>'
)
html, count = re.subn(r'<aside class="objection">.*?</aside>', transfer_case, html, count=1, flags=re.S)
if count != 1:
    raise SystemExit("Expected one objection panel to replace")

footer = (
    '<footer class="footer"><div class="footer-rule" aria-hidden="true"></div>'
    '<div class="footer-main"><div><strong>Independent candidate vision by Russell Dudek</strong><br>'
    'Currently based in Pittsburgh and actively relocating to the Tampa Bay area.<br>'
    '<a href="tel:+14122878640">412.287.8640</a> · '
    '<a href="mailto:russelldudek@gmail.com">russelldudek@gmail.com</a> · '
    '<a href="https://www.linkedin.com/in/russelldudek">LinkedIn</a></div>'
    '<div class="footer-descriptor"><span>AI Service Operations</span>'
    '<small>Run it inside. Make it repeatable outside.</small></div></div></footer>'
)
html, count = re.subn(r'<footer class="footer">.*?</footer>', footer, html, count=1, flags=re.S)
if count != 1:
    raise SystemExit("Expected one footer to replace")

marker = "/* XTIUM SERVICE TRANSLATION SPINE — USER-APPROVED CORRECTION */"
if marker not in css:
    css += r'''

/* XTIUM SERVICE TRANSLATION SPINE — USER-APPROVED CORRECTION */
.translation-spine{
  position:relative;
  min-height:0;
  display:grid;
  grid-template-columns:minmax(0,1fr) 116px minmax(0,1fr);
  align-items:stretch;
  gap:0;
  overflow:hidden;
  border:1px solid var(--xtium-line);
  background:#fff;
  box-shadow:0 26px 70px rgba(23,107,117,.12);
}
.translation-spine .plate{
  position:static;
  width:auto;
  min-height:0;
  padding:1.45rem;
  border:0;
  background:#fff;
  box-shadow:none;
  opacity:1;
  transform:none!important;
}
.translation-spine .plate.left{grid-column:1;border-right:1px solid var(--xtium-line)}
.translation-spine .plate.right{grid-column:3;border-left:1px solid var(--xtium-line)}
.translation-spine .plate h2{font-size:1.55rem;margin:.55rem 0 1.1rem}
.translation-spine .spec-list{display:grid;grid-template-rows:repeat(4,minmax(92px,auto));gap:0}
.translation-spine .spec-row{
  position:relative;
  display:grid;
  grid-template-columns:82px 1fr;
  gap:.7rem;
  align-items:start;
  padding:1rem 0;
  border-top:1px solid var(--xtium-line);
  font-size:.8rem;
  background:transparent;
}
.translation-spine .spec-row b{font-size:.67rem;letter-spacing:.08em}
.translation-spine .registration-mark{
  position:static;
  grid-column:2;
  grid-row:1;
  z-index:1;
  display:flex;
  align-items:center;
  justify-content:center;
  padding:1rem .75rem;
  pointer-events:none;
  background:linear-gradient(180deg,var(--xtium-teal),var(--xtium-ink) 48%,var(--xtium-orange));
}
.translation-spine .registration-mark span{
  width:auto;
  height:auto;
  border:0;
  background:transparent;
  box-shadow:none;
  color:#fff;
  writing-mode:vertical-rl;
  transform:rotate(180deg);
  font-size:.7rem;
  font-weight:800;
  letter-spacing:.14em;
  line-height:1.45;
}
.translation-spine .right .spec-row::before{
  content:"→";
  position:absolute;
  z-index:3;
  left:-72px;
  top:50%;
  transform:translateY(-50%);
  width:28px;
  height:28px;
  display:grid;
  place-items:center;
  border-radius:50%;
  background:#fff;
  color:var(--xtium-orange);
  font-weight:900;
  box-shadow:0 0 0 1px rgba(255,255,255,.48);
}
.translation-spine .left .spec-row{animation:inside-proof .9s ease both}
.translation-spine .right .spec-row{animation:customer-pattern .9s ease both}
.translation-spine .spec-row:nth-child(1){animation-delay:.25s}
.translation-spine .right .spec-row:nth-child(1){animation-delay:.6s}
.translation-spine .spec-row:nth-child(2){animation-delay:1.55s}
.translation-spine .right .spec-row:nth-child(2){animation-delay:1.9s}
.translation-spine .spec-row:nth-child(3){animation-delay:2.85s}
.translation-spine .right .spec-row:nth-child(3){animation-delay:3.2s}
.translation-spine .spec-row:nth-child(4){animation-delay:4.15s}
.translation-spine .right .spec-row:nth-child(4){animation-delay:4.5s}
@keyframes inside-proof{0%{background:transparent}45%{background:rgba(17,183,179,.13)}100%{background:transparent}}
@keyframes customer-pattern{0%{background:transparent}45%{background:rgba(255,122,0,.12)}100%{background:transparent}}
.transfer-case{
  align-self:start;
  padding:2.25rem;
  border-left:7px solid var(--xtium-teal);
  background:#fff;
  color:var(--xtium-ink);
  box-shadow:0 20px 50px rgba(17,19,24,.08);
}
.transfer-case h3{font-size:2rem;line-height:1.08;margin:.2rem 0 1rem}
.transfer-case p{color:#4f5b63}
.transfer-case strong{color:var(--xtium-ink)}
.footer{display:block;padding:0;background:#0b0d10;color:#bfc6ca}
.footer-rule{height:4px;background:linear-gradient(90deg,var(--xtium-teal) 0 52%,var(--xtium-orange) 52% 100%)}
.footer-main{display:flex;justify-content:space-between;gap:2rem;align-items:flex-end;padding:2.6rem clamp(1.25rem,6vw,6.5rem)}
.footer-descriptor{display:grid;gap:.25rem;text-align:right}
.footer-descriptor span{color:#fff;font-size:.78rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase}
.footer-descriptor small{color:#8f999f}
.footer img{display:none!important}
@media(max-width:700px){
  .translation-spine{grid-template-columns:1fr;overflow:visible}
  .translation-spine .plate.left{grid-column:1;grid-row:1;border-right:0}
  .translation-spine .registration-mark{grid-column:1;grid-row:2;min-height:74px;background:linear-gradient(90deg,var(--xtium-teal),var(--xtium-ink) 48%,var(--xtium-orange))}
  .translation-spine .registration-mark span{writing-mode:horizontal-tb;transform:none;text-align:center}
  .translation-spine .plate.right{grid-column:1;grid-row:3;border-left:0}
  .translation-spine .right .spec-row::before{content:"↓";left:50%;top:-15px;transform:translateX(-50%)}
  .translation-spine .spec-list{grid-template-rows:none}
  .footer-main{display:grid;gap:1.5rem}
  .footer-descriptor{text-align:left}
}
@media(prefers-reduced-motion:reduce){
  .translation-spine .spec-row{animation:none!important;transition:none!important}
}
'''

index_path.write_text(html, encoding="utf-8")
styles_path.write_text(css, encoding="utf-8")

checks = {
    "translation spine class": 'class="register translation-spine ready"' in html,
    "four operating rows": html.count('class="spec-row"') == 8,
    "positive transfer heading": "Why the experience transfers" in html,
    "negative panel removed": 'class="objection"' not in html,
    "footer logo removed": '<footer class="footer">' in html and '<footer class="footer"><div class="footer-rule"' in html,
    "footer descriptor": "AI Service Operations" in html,
    "CSS correction marker": marker in css,
}
failed = [name for name, passed in checks.items() if not passed]
if failed:
    raise SystemExit("Hero repair assertions failed: " + ", ".join(failed))
print("Approved XTIUM hero, transfer framing, and footer repair applied.")
