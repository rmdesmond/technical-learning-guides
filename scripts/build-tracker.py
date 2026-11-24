"""Build cards/learning-guide-tracker.pdf from the guides in guides/.

One row per guide PDF (learning guide, matn, Beyond the Basics, Way Beyond the
Basics), in the README's reading order, one box per page.

Usage: python3 scripts/build-tracker.py [output.pdf]
Needs: pip install -r scripts/requirements.txt
When you add a subject, add it to NAMES and ORDER below.
"""
import sys, glob, os, datetime
import pypdf
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black

repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(repo, "cards", "learning-guide-tracker.pdf")
DATE = datetime.date.today().isoformat()

NAMES = {
    "linux-command-line": "Linux Command Line", "bash": "Bash", "markdown": "Markdown",
    "git": "Git", "vim": "Vim", "ai": "AI", "c": "C", "cpp": "C++",
    "systems-programming": "Systems Programming", "make": "Make", "cmake": "CMake",
    "clang-format": "clang-format", "google-test": "Google Test",
    "sil": "Software-in-the-Loop (SIL)", "hil": "Hardware-in-the-Loop (HIL)",
    "vm": "Virtual Machines", "docker": "Docker", "ci-cd-pipeline": "CI/CD Pipelines",
    "signed-releases": "Signed Releases", "web-protocols": "Web Protocols", "ocpp": "OCPP",
    "linux-vs-rtos": "Linux vs. RTOS", "yocto": "Yocto", "i2c-linux": "I2C on Linux",
    "functional-safety": "Functional Safety",
}
# reading order inside each group, matching README
ORDER = ["linux-command-line", "bash", "markdown", "git", "vim", "ai",
         "c", "cpp", "systems-programming",
         "make", "cmake", "clang-format", "google-test", "sil", "hil",
         "vm", "docker", "ci-cd-pipeline", "signed-releases",
         "web-protocols", "ocpp",
         "linux-vs-rtos", "yocto", "i2c-linux", "functional-safety"]
TYPES = [("-learning-guide.pdf", ""), ("-matn.pdf", " · Matn"),
         ("-beyond-the-basics-learning-guide.pdf", " · Beyond"),
         ("-way-beyond-the-basics-learning-guide.pdf", " · Way Beyond")]

rows, groups = [], []  # (label, pages, group)
for subj in ORDER:
    d = glob.glob(os.path.join(repo, "guides", "*", subj))[0]
    group = os.path.basename(os.path.dirname(d))
    for suffix, tag in TYPES:
        f = os.path.join(d, subj + suffix)
        if os.path.exists(f):
            rows.append((NAMES[subj] + tag, len(pypdf.PdfReader(f).pages), group))
n_base = sum(1 for r in rows if "·" not in r[0])

W, H = landscape(letter)
c = canvas.Canvas(out, pagesize=(W, H))
c.setTitle("Learning Guide Tracker"); c.setAuthor("(anonymous)")
c.setSubject("unspecified"); c.setCreator("anonymous")
grey, light, faint = HexColor("#9a9a9a"), HexColor("#f2f2f2"), HexColor("#bdbdbd")
L, R = 36, W - 36
c.setFont("Helvetica-Bold", 17); c.drawString(L, H - 50, "Learning Guide Tracker")
c.setFont("Helvetica", 9); c.drawRightString(R - 110, H - 50, "Name:")
c.setLineWidth(0.6); c.line(R - 105, H - 51, R, H - 51)
c.setFont("Helvetica", 7.5); c.setFillColor(grey)
c.drawString(L, H - 63, f"As of {DATE}  ·  one box per page  ·  tick a box when you've finished that page  "
             "·  rows follow the reading order in the README  ·  blank rows are for guides that don't exist yet")

NCOL, nameW, ppW = 40, 132, 24
gx = L + nameW + ppW
cell = (R - gx) / NCOL
nblank = 4
top = H - 84
rowh = min(13.0, (top - 40 - 12) / (len(rows) + nblank + 1))
box = min(cell, rowh) - 2.2

c.setFillColor(black); c.setFont("Helvetica-Bold", 7.5); c.drawString(L, top - 9, "Learning guide")
c.setFont("Helvetica", 5.5); c.setFillColor(grey)
for i in range(NCOL):
    c.drawCentredString(gx + cell * i + cell / 2, top - 9, str(i + 1))
c.setStrokeColor(black); c.setLineWidth(0.8); c.line(L, top - 12, R, top - 12)

y = top - 12
prev = None
for label, pages, group in rows:
    if prev and group != prev:
        c.setStrokeColor(black); c.setLineWidth(0.6); c.line(L, y, R, y)
    prev = group
    y -= rowh
    isbase = "·" not in label
    c.setFillColor(black if isbase else HexColor("#555555"))
    c.setFont("Helvetica-Bold" if isbase else "Helvetica", 7)
    c.drawString(L + 2, y + rowh / 2 - 2.4, label)
    c.setFont("Helvetica", 5.5); c.setFillColor(grey)
    c.drawRightString(gx - 4, y + rowh / 2 - 2, f"{pages} pp")
    for i in range(NCOL):
        bx = gx + cell * i + (cell - box) / 2; by = y + (rowh - box) / 2
        if i < pages:
            c.setStrokeColor(black); c.setLineWidth(0.5); c.rect(bx, by, box, box)
            c.setFont("Helvetica", 3.6); c.setFillColor(grey); c.drawString(bx + 0.8, by + box - 4, str(i + 1))
        else:
            c.setFillColor(light); c.rect(gx + cell * i, y, cell, rowh, stroke=0, fill=1)
    c.setStrokeColor(HexColor("#e3e3e3")); c.setLineWidth(0.3); c.line(L, y, gx, y)
c.setStrokeColor(black); c.setLineWidth(0.8); c.line(L, y, R, y)
for _ in range(nblank):
    y -= rowh
    c.setStrokeColor(faint); c.setLineWidth(0.4); c.line(L, y, gx - 6, y)
    c.setStrokeColor(black); c.setLineWidth(0.5)
    for i in range(NCOL):
        c.rect(gx + cell * i + (cell - box) / 2, y + (rowh - box) / 2, box, box)

c.setFont("Helvetica", 6.5); c.setFillColor(grey)
n_matn = sum("Matn" in r[0] for r in rows); n_beyond = sum("Beyond" in r[0] for r in rows)
c.drawString(L, 30, f"{n_base} learning guides, {n_matn} matns and {n_beyond} Beyond the Basics guide{'' if n_beyond == 1 else 's'} as of {DATE}. "
             "Cards (Git Habit Card, this tracker) and START-HERE.pdf are references, not guides, and aren't tracked here.")
c.save()
print(f"wrote {out}: {len(rows)} rows")
