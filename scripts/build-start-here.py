"""Build START-HERE.pdf, the one-page onboarding sheet in the repo root.

Usage: python3 scripts/build-start-here.py [output.pdf]
Needs: pip install -r scripts/requirements.txt
When you add a group or subject, update the reading-order table (rows) below.
"""
import sys, os, datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
                                Table, TableStyle, Flowable, Preformatted)

repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(repo, "START-HERE.pdf")
MONTH = datetime.date.today().strftime("%B %Y")
BLUE, ORANGE = HexColor("#1f4e79"), HexColor("#c55a11")
INFO_BG, TRAP_BG, CODE_BG = HexColor("#e8f0f8"), HexColor("#e8f0f8"), HexColor("#f2f2f2")
GREY = HexColor("#666666")

body = ParagraphStyle("b", fontName="Helvetica", fontSize=8.3, leading=10.4)
lead = ParagraphStyle("l", parent=body, fontSize=9.6, leading=12, textColor=HexColor("#333333"))
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=19, leading=22, textColor=BLUE)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=10.8, leading=13, textColor=BLUE,
                    spaceBefore=4, spaceAfter=1.5)
cap = ParagraphStyle("cap", parent=body, fontName="Helvetica-Oblique", fontSize=7.3, leading=9,
                     textColor=GREY, spaceAfter=3)
code = ParagraphStyle("code", fontName="Courier", fontSize=7.3, leading=8.6)
cell = ParagraphStyle("cell", parent=body, fontSize=8, leading=9.6)

def C(t): return f'<font face="Courier">{t}</font>'

class Box(Flowable):
    """Tinted box with coloured left rule (callout) or plain grey box (code)."""
    def __init__(self, inner, bg, rule=None, pad=4.5):
        super().__init__(); self.inner, self.bg, self.rule, self.pad = inner, bg, rule, pad
    def wrap(self, aw, ah):
        self.aw = aw; _, h = self.inner.wrap(aw - 2 * self.pad - 4, ah); self.h = h + 2 * self.pad
        return aw, self.h
    def draw(self):
        c = self.canv; c.setFillColor(self.bg)
        if self.rule:
            c.rect(0, 0, self.aw, self.h, stroke=0, fill=1)
            c.setFillColor(self.rule); c.rect(0, 0, 3, self.h, stroke=0, fill=1)
        else:
            c.setStrokeColor(HexColor("#cccccc")); c.setLineWidth(0.5); c.rect(0, 0, self.aw, self.h, stroke=1, fill=1)
        self.inner.drawOn(c, self.pad + 4, self.pad)

def codeblock(caption, text):
    return [Paragraph(caption, cap), Box(Preformatted(text, code), CODE_BG), Spacer(1, 3)]

def callout(text, rule):
    return [Spacer(1, 3), Box(Paragraph(text, body), INFO_BG, rule), Spacer(1, 2)]

class Check(Flowable):
    def __init__(self, text):
        super().__init__(); self.p = Paragraph(text, body)
    def wrap(self, aw, ah):
        self.aw = aw; _, h = self.p.wrap(aw - 18, ah); self.h = h + 3.5; return aw, self.h
    def draw(self):
        c = self.canv; c.setStrokeColor(black); c.setLineWidth(0.7)
        c.rect(1, self.h - 11.5, 8, 8); self.p.drawOn(c, 18, 3.5)

story = [
    Paragraph("Start here: getting the learning guides", h1), Spacer(1, 2),
    Paragraph("You have never used Git or GitHub. That is fine: the first thing you will learn is how to fetch this "
              "collection, and the guides take it from there. Budget twenty minutes.", lead),

    Paragraph("1. Install Git (one time)", h2),
    Paragraph("Git is the program that copies a project from GitHub to your computer and keeps the copy up to date. "
              "Install it, then open a terminal (Terminal on macOS, PowerShell or Git Bash on Windows, any terminal on "
              "Linux) and check it answers:", body),
    *codeblock("Verify the install before going further.",
               "# macOS:   xcode-select --install\n"
               "# Windows: install from https://git-scm.com/download/win\n"
               "# Ubuntu:  sudo apt install git\n"
               "git --version\n"
               "# expected: git version 2.4x.x  (any 2.x is fine)"),

    Paragraph("2. Fetch the repo (one time)", h2),
    Paragraph(f'"Cloning" copies the whole collection, including its history, into a new folder named '
              f'{C("technical-learning-guides")} inside wherever your terminal currently is:', body),
    *codeblock("You should see README.md, START-HERE.pdf, guides/, cards/ and prompts/.",
               "cd ~                                   # go to your home folder\n"
               "git clone https://github.com/rmdesmond/technical-learning-guides.git\n"
               "cd technical-learning-guides\n"
               "ls                                     # dir on Windows PowerShell also works"),
    *callout("<b>No login needed.</b> You do not need a GitHub account to clone a public repo, and you will not be "
             "asked for a password. If the command asks for one, the address is wrong or the repo is private; check "
             "the spelling with whoever gave you the link.", BLUE),

    Paragraph("3. Read the README, then open your first guide", h2),
    Paragraph(f"{C('README.md')} is a plain-text file; open it in any editor, or read it on the repo's GitHub page "
              f"where it is rendered nicely. It holds the catalogue table. The folders under {C('guides/')} are "
              f"numbered in the intended order, and each subject has its own folder. Open the file ending "
              f"{C('-learning-guide.pdf')} first. A subject folder may also hold a {C('-matn.pdf')} (a few pages "
              f"to memorise once you have done the guide) and a Beyond the Basics guide (the next level). "
              f"The checkboxes are there to be ticked on screen or on paper.", body),
    Spacer(1, 3),
]

rows = [
    ("1-foundations: Linux command line, Bash, Markdown, Git, Vim, AI",
     "You already live in a terminal and have committed to a repo before."),
    ("2-languages: C, C++, systems programming", "You are here for infrastructure only; jump to 4."),
    ("3-build-and-test: Make, CMake, clang-format, Google Test, SIL, HIL",
     "You have not done 2; these assume you can write a small C/C++ program."),
    ("4-systems-and-infra: VMs, Docker, CI/CD pipelines, signed releases",
     "Nothing. Everyone needs these eventually; do them in that order."),
    ("5-web: web protocols, OCPP", "Your work never touches HTTP. (It will.)"),
    ("6-embedded: Linux vs. RTOS, Yocto, I2C on Linux, functional safety",
     "Your software never runs on a device of its own. These assume C and the Linux command line."),
]
data = [[Paragraph("<b>Go in this order</b>", cell), Paragraph("<b>Skip it if</b>", cell)]]
for a, b in rows:
    g, rest = a.split(":", 1)
    data.append([Paragraph(f"<b>{g}</b>:{rest}", cell), Paragraph(b, cell)])
t = Table(data, colWidths=[3.25 * 72, 3.25 * 72])
t.setStyle(TableStyle([
    ("LINEBELOW", (0, 0), (-1, 0), 0.9, BLUE), ("LINEBELOW", (0, 1), (-1, -1), 0.4, HexColor("#cccccc")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 1.8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 1.8), ("BACKGROUND", (0, 0), (-1, 0), INFO_BG)]))
story += [t,
    Paragraph("4. Keep your copy current", h2),
    Paragraph("Guides get revised. Whenever you come back, run one command from inside the folder and any updated "
              "PDFs replace themselves:", body),
    *codeblock('"Already up to date." means nothing changed.',
               "cd ~/technical-learning-guides\ngit pull"),
    Paragraph("Before you open the first guide", h2),
    Check(f"{C('git --version')} prints a version number."),
    Check(f"{C('~/technical-learning-guides/README.md')} exists and I have read its catalogue table."),
    Check("I have a PDF viewer that lets me tick checkboxes, or a printer."),
    Check("I know which group folder I am starting in and why (the table above)."),
    Check("I know how to report a mistake: open an issue on the repo, title it with the guide name and chapter number."),
    *callout("<b>One habit.</b> Do not read a guide first. Open it, set up the tool using its \"Before you start\" page, "
             "and type every example. Each chapter builds on the last, so the order inside a guide is not negotiable; "
             "the order between guides is.", ORANGE),
]

def footer(c, d):
    c.saveState(); c.setFont("Helvetica", 7.5); c.setFillColor(GREY)
    c.drawString(0.6 * 72, 0.45 * 72, "Start here: getting the learning guides")
    c.drawRightString(letter[0] - 0.6 * 72, 0.45 * 72, MONTH); c.restoreState()

doc = BaseDocTemplate(out, pagesize=letter, leftMargin=0.7 * 72, rightMargin=0.7 * 72,
                      topMargin=0.45 * 72, bottomMargin=0.62 * 72,
                      title="Start here: getting the learning guides", author="(anonymous)")
doc.addPageTemplates([PageTemplate(frames=[Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")],
                                   onPage=footer)])
doc.build(story)
import pypdf
n = len(pypdf.PdfReader(out).pages)
print(f"wrote {out}: {n} page(s)")
if n != 1:
    sys.exit("START-HERE.pdf should fit on one page; tighten the text or spacing")
