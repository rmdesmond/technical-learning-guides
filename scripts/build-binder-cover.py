"""Build cards/binder-cover.pdf, the printable cover for a binder of guides.

The cover groups the guides by stage of the software journey (not by the
numbered folders in guides/). When you add a guide, add its chip to STAGES.

Usage: python3 scripts/build-binder-cover.py [output.pdf]
Needs: pip install -r scripts/requirements.txt
"""
import os, sys, datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth

repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(repo, "cards", "binder-cover.pdf")
UPDATED = datetime.date.today().strftime("%B %Y")

NAVY, TEAL, ORANGE = HexColor("#1c2a42"), HexColor("#2a9d8f"), HexColor("#f0a030")
INK, MUTED, RULE = HexColor("#1c2a42"), HexColor("#6b7280"), HexColor("#e5e7eb")
CHIP, SPINE, CREAM = HexColor("#eef0f3"), HexColor("#d1d5db"), HexColor("#fff4e0")

STAGES = [
    ("Think & write", "Capture ideas, notes and docs in a form that survives.",
     ["Markdown", "AI", "Vim"]),
    ("Build", "Turn source into something that runs, repeatably.",
     ["C", "C++", "Systems programming", "Make", "CMake", "clang-format"]),
    ("Test", "Prove it works before anyone depends on it.",
     ["Google Test", "SIL", "HIL", "Functional safety"]),
    ("Version", "Keep every change, undo any mistake, work with others.",
     ["Git", "Git habits", "Signed releases"]),
    ("Run anywhere", "Make the same software behave the same on any machine.",
     ["Linux command line", "Bash", "Virtual machines", "Docker"]),
    ("Run on hardware", "Put software on a device of its own and keep its promises.",
     ["Linux vs. RTOS", "Yocto", "I2C on Linux"]),
    ("Ship & connect", "Deliver automatically and talk to the rest of the world.",
     ["CI/CD pipelines", "Web protocols", "OCPP"]),
]

W, H = letter
L, R = 54, W - 54
c = canvas.Canvas(out, pagesize=letter)
c.setTitle("Introducing Software Tools & Concepts"); c.setAuthor("(anonymous)")
c.setSubject("Binder cover for the technical learning guides"); c.setCreator("(anonymous)")

# Header band
band = 165
c.setFillColor(NAVY); c.rect(0, H - band, W, band, stroke=0, fill=1)
c.setFillColor(TEAL); c.rect(0, H - band - 6, W, 6, stroke=0, fill=1)
kicker = c.beginText(L, H - 40)
kicker.setFont("Helvetica-Bold", 9.5); kicker.setCharSpace(4); kicker.setFillColor(HexColor("#7fd1c7"))
kicker.textOut("A BINDER OF LEARNING GUIDES"); kicker.setCharSpace(0); c.drawText(kicker)
c.setFillColor(white); c.setFont("Helvetica-Bold", 30)
c.drawString(L, H - 78, "Introducing Software Tools &")
c.drawString(L, H - 110, "Concepts")
c.setFillColor(HexColor("#d7dde6")); c.setFont("Helvetica", 12.5)
c.drawString(L, H - 136, "Learning guides for the whole software development and deployment journey")

# Intro with teal rule
y = H - band - 28
intro = ["Every guide starts with the problem a tool solves, before any syntax. Then the smallest working example,",
         "the one mental model that makes it click, and what to deliberately skip at first. One new idea per chapter,",
         "until a beginner can use the tool unaided on a real project."]
c.setFillColor(TEAL); c.rect(L, y - 38, 3, 50, stroke=0, fill=1)
c.setFillColor(INK); c.setFont("Helvetica", 9.6)
for i, line in enumerate(intro):
    c.drawString(L + 13, y - i * 14.5, line)

# Stages
x_num, x_txt = L + 21, L + 52
row = 60
top = y - 48
spine_top, spine_bot = top - 14, top - 14 - row * len(STAGES)
c.setStrokeColor(SPINE); c.setLineWidth(2); c.line(x_num, spine_top, x_num, spine_bot + 3)
for i, (name, blurb, chips) in enumerate(STAGES):
    ty = top - i * row
    c.setFillColor(white); c.setStrokeColor(TEAL); c.setLineWidth(2)
    c.circle(x_num, ty - 13, 11, stroke=1, fill=1)
    c.setFillColor(TEAL); c.setFont("Helvetica-Bold", 9.5); c.drawCentredString(x_num, ty - 16.3, str(i + 1))
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 14); c.drawString(x_txt, ty - 9, name)
    c.setFillColor(MUTED); c.setFont("Helvetica", 8.8); c.drawString(x_txt, ty - 23, blurb)
    cx = x_txt
    for chip in chips:
        w = stringWidth(chip, "Helvetica-Bold", 8.6) + 16
        c.setFillColor(CHIP); c.roundRect(cx, ty - 47, w, 16, 8, stroke=0, fill=1)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 8.6); c.drawString(cx + 8, ty - 42.5, chip)
        cx += w + 6
    if i < len(STAGES) - 1:
        c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(x_txt, ty - 53, R, ty - 53)

# More to come
my = spine_bot + 12
c.setStrokeColor(ORANGE); c.setLineWidth(2); c.setDash(2, 2.5)
c.circle(x_num, my - 20, 11, stroke=1, fill=0); c.setDash()
c.setFillColor(ORANGE); c.setFont("Helvetica-Bold", 9); c.drawCentredString(x_num, my - 23, "...")
c.setFillColor(CREAM); c.roundRect(x_txt - 6, my - 46, R - x_txt + 6, 50, 4, stroke=0, fill=1)
c.setFillColor(ORANGE); c.rect(x_txt - 6, my - 46, 3, 50, stroke=0, fill=1)
c.setFont("Helvetica-Bold", 10); c.drawString(x_txt + 6, my - 12, "MORE TO COME")
c.setFillColor(INK); c.setFont("Helvetica-Oblique", 9.2)
c.drawString(x_txt + 6, my - 26, "A growing collection. New guides are added as the journey continues, and each subject")
c.drawString(x_txt + 6, my - 38, "can grow a matn and deeper guides of its own.")

# Footer
fy = 50
c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(L, fy + 18, R, fy + 18)
c.setFillColor(MUTED); c.setFont("Helvetica", 8.3)
c.drawString(L, fy + 4, "Four guide types per subject:  learning guide  |  matn  |  Beyond the Basics  |  Way Beyond the Basics")
c.drawString(L, fy - 8, f"Started October 2026  ·  Updated {UPDATED}")
c.save()
print(f"wrote {out}")
