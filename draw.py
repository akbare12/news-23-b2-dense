#!/usr/bin/env python3
"""Draw the 23 Nov 2026 world-news front page (1024x1024) with PIL."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

INK = (17, 17, 17)
PAPER = (255, 255, 255)
RED = (185, 28, 28)
NAVY = (30, 58, 95)
TEAL = (15, 118, 110)
AMBER = (180, 83, 9)
GREEN = (21, 128, 61)
BLUE = (29, 78, 216)
GRAY = (107, 114, 128)
LGRAY = (243, 244, 246)
MAP_BG = (220, 230, 240)
LAND = (232, 232, 224)
LAND_EDGE = (160, 160, 150)
YELLOW_BG = (254, 243, 199)
GOLD = (146, 64, 14)

FD = "/usr/share/fonts/truetype/dejavu/"
def F(name, size):
    return ImageFont.truetype(FD + name, size)

f_mast = F("DejaVuSerif-Bold.ttf", 46)
f_mast_date = F("DejaVuSans-Bold.ttf", 24)
f_kick = F("DejaVuSans-Bold.ttf", 11)
f_hero = F("DejaVuSans-Bold.ttf", 27)
f_hero_big = F("DejaVuSans-Bold.ttf", 58)
f_banner = F("DejaVuSans-Bold.ttf", 21)
f_sec = F("DejaVuSans-Bold.ttf", 12)
f_head = F("DejaVuSans-Bold.ttf", 11)
f_body = F("DejaVuSans.ttf", 9)
f_meta = F("DejaVuSans.ttf", 9)
f_small = F("DejaVuSans.ttf", 9)
f_num = F("DejaVuSans-Bold.ttf", 19)
f_numlab = F("DejaVuSans.ttf", 9)
f_pin = F("DejaVuSans-Bold.ttf", 8)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def trunc(lines, n):
    if len(lines) > n:
        lines = lines[:n]
        lines[-1] = lines[-1].rsplit(" ", 1)[0] + " ..."
    return lines

def badge(x, y, label, color):
    w = d.textlength(label, font=f_meta) + 10
    d.rounded_rectangle([x, y, x + w, y + 13], radius=3, fill=color)
    d.text((x + 5, y + 1), label, font=f_meta, fill=PAPER)
    return w

def chip(x, y, label, color):
    w = d.textlength(label, font=f_meta) + 10
    d.rounded_rectangle([x, y, x + w, y + 13], radius=3, fill=color)
    d.text((x + 5, y + 1), label, font=f_meta, fill=PAPER)
    return x + w

# ---------------- masthead ----------------
d.rectangle([0, 0, W, 5], fill=INK)
d.rectangle([0, 5, W, 8], fill=RED)
d.text((10, 12), "THE WORLD TODAY", font=f_mast, fill=INK)
d.text((W - 10 - d.textlength("MONDAY 23 NOVEMBER 2026", font=f_mast_date), 16),
       "MONDAY 23 NOVEMBER 2026", font=f_mast_date, fill=RED)
d.text((W - 10 - d.textlength("MONDAY EDITION  ·  ALL TIMES GMT", font=f_small), 48),
       "MONDAY EDITION  ·  ALL TIMES GMT", font=f_small, fill=GRAY)
d.line([10, 66, W - 10, 66], fill=INK, width=2)

# meta strip + legend
d.text((10, 72), "31 STORIES  ·  6 REGIONS  ·  EVERY ITEM DATED 23 NOV",
       font=f_kick, fill=INK)
lx = W - 10
for lab, col in [("ONGOING", BLUE), ("DENIAL", RED), ("CLAIM", AMBER), ("REPORTED", GREEN)]:
    w = d.textlength(lab, font=f_meta) + 10
    lx -= w + 6
    d.rounded_rectangle([lx, 72, lx + w, 85], radius=3, fill=col)
    d.text((lx + 5, 73), lab, font=f_meta, fill=PAPER)
d.line([10, 90, W - 10, 90], fill=INK, width=1)

# ---------------- hero row ----------------
HY, HH = 96, 150
# hero 1: Kospi
x0, y0, x1, y1 = 10, HY, 508, HY + HH
d.rectangle([x0, y0, x1, y1], outline=INK, width=2)
d.rectangle([x0, y0, x1, y0 + 20], fill=INK)
d.text((x0 + 8, y0 + 3), "MARKETS  ·  SEOUL", font=f_kick, fill=(255, 255, 255))
badge(x1 - 78, y0 + 4, "REPORTED", GREEN)
d.text((x0 + 8, y0 + 26), "AI ROUT HITS ASIA", font=f_hero, fill=INK)
d.text((x0 + 8, y0 + 56), "-3.3%", font=F("DejaVuSans-Bold.ttf", 46), fill=RED)
d.text((x0 + 160, y0 + 64), "KOSPI", font=F("DejaVuSans-Bold.ttf", 20), fill=INK)
d.text((x0 + 160, y0 + 90), "closes 4,708.54", font=f_body, fill=GRAY)
# mini falling chart
cx0, cy0, cx1, cy1 = x0 + 330, y0 + 30, x1 - 12, y0 + 96
d.rectangle([cx0, cy0, cx1, cy1], outline=GRAY, width=1)
pts = [(cx0 + i * (cx1 - cx0) / 9, cy0 + 6 + (i * i) * (cy1 - cy0 - 12) / 81)
       for i in range(10)]
d.line(pts, fill=RED, width=3)
d.text((cx0, cy1 + 2), "FRI -5.2%  →  MON -3.3%", font=f_meta, fill=GRAY)
d.text((cx0, cy1 + 13), "Samsung -3.1%  ·  SK Hynix -2.5%", font=f_meta, fill=GRAY)
body = wrap("Kospi sheds 161 pts, intraday -5.8%, as the AI sell-off spreads from Wall Street.", f_body, x1 - x0 - 16)
body = trunc(body, 1)
yy = y0 + 126
for ln in body:
    d.text((x0 + 8, yy), ln, font=f_body, fill=INK)
    yy += 11
d.text((x0 + 8, y0 + 140), "Korea JoongAng Daily  ·  CNBC  ·  Morningstar",
       font=f_meta, fill=GRAY)

# hero 2: Guterres / Barbados
x0, y0, x1, y1 = 516, HY, 1014, HY + HH
d.rectangle([x0, y0, x1, y1], outline=INK, width=2)
d.rectangle([x0, y0, x1, y0 + 20], fill=NAVY)
d.text((x0 + 8, y0 + 3), "UNITED NATIONS  ·  BARBADOS", font=f_kick, fill=(255, 255, 255))
badge(x1 - 78, y0 + 4, "REPORTED", GREEN)
d.text((x0 + 8, y0 + 26), "GUTERRES: REGULATE", font=f_hero, fill=INK)
d.text((x0 + 8, y0 + 56), "AI BEFORE IT'S TOO LATE", font=f_hero, fill=INK)
# podium icon
px, py = x1 - 108, y0 + 92
d.rectangle([px, py, px + 96, py + 52], outline=NAVY, width=2)
d.ellipse([px + 38, py - 12, px + 58, py + 8], fill=NAVY)
d.polygon([(px + 30, py + 4), (px + 66, py + 4), (px + 58, py + 52), (px + 38, py + 52)],
          fill=NAVY)
d.text((px + 8, py + 16), "UN", font=F("DejaVuSans-Bold.ttf", 16), fill=PAPER)
d.text((px - 4, py + 56), "BRIDGETOWN SUMMIT", font=f_meta, fill=GRAY)
body = wrap("UN chief urges global AI safety rules at the Bridgetown summit. 150 delegates back a risk framework — a blueprint, not a treaty.", f_body, 330)
body = trunc(body, 3)
yy = y0 + 92
for ln in body:
    d.text((x0 + 8, yy), ln, font=f_body, fill=INK)
    yy += 11
d.text((x0 + 8, y1 - 13), "UN News  ·  UN Web TV", font=f_meta, fill=GRAY)

# ---------------- Lowy banner ----------------
BY, BH = 254, 60
d.rectangle([10, BY, 1014, BY + BH], fill=NAVY)
d.text((18, BY + 4), "ASIA POWER INDEX 2026", font=f_kick, fill=(255, 210, 100))
d.text((18, BY + 19), "US LEAD OVER CHINA AT RECORD LOW", font=F("DejaVuSans-Bold.ttf", 20), fill=PAPER)
# bars
bx, by = 620, BY + 8
d.text((bx, by), "US 78.9", font=f_kick, fill=PAPER)
d.rectangle([bx, by + 14, bx + 200, by + 24], fill=(255, 255, 255))
d.text((bx, by + 28), "CHINA 73.6", font=f_kick, fill=(255, 210, 100))
d.rectangle([bx, by + 42, bx + 186, by + 52], fill=(255, 210, 100))
d.text((838, BY + 8), "GAP 5.3", font=F("DejaVuSans-Bold.ttf", 20), fill=(255, 210, 100))
d.text((838, BY + 32), "narrowest since 2018", font=f_meta, fill=PAPER)
d.text((18, BY + 44), "US diplomatic influence -6 to 76.7  ·  India 3rd at 40.5  ·  Published Sun, reported Mon",
       font=f_meta, fill=(200, 210, 230))

# ---------------- map row ----------------
MY, MH = 320, 158
d.rectangle([10, MY, 648, MY + MH], outline=INK, width=1)
d.text((18, MY + 5), "WHERE IT HAPPENED — EVERY STORY PINNED",
       font=f_kick, fill=INK)
d.text((18, MY + 5), "WHERE IT HAPPENED — EVERY STORY PINNED",
       font=f_kick, fill=INK)
# map area
mx0, my0, mx1, my1 = 16, MY + 24, 642, MY + MH - 20
d.rectangle([mx0, my0, mx1, my1], fill=MAP_BG)

def proj(lon, lat):
    x = mx0 + (lon + 180.0) / 360.0 * (mx1 - mx0)
    y = my0 + (72.0 - lat) / 130.0 * (my1 - my0)
    return x, y

CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 70), (-75, 72), (-65, 60), (-55, 52), (-60, 45), (-70, 42), (-75, 35), (-80, 25), (-90, 21), (-97, 16), (-105, 20), (-115, 28), (-125, 40), (-130, 55), (-150, 60), (-165, 60)],
    [(-55, 60), (-45, 60), (-40, 65), (-30, 68), (-20, 70), (-25, 76), (-40, 80), (-55, 76), (-58, 70)],
    [(-80, 10), (-75, 5), (-70, 0), (-60, -5), (-50, -5), (-40, -10), (-35, -15), (-40, -25), (-48, -28), (-55, -35), (-65, -45), (-70, -55), (-73, -40), (-72, -20), (-80, -5), (-81, 5)],
    [(-10, 36), (-5, 44), (0, 46), (5, 44), (10, 45), (15, 40), (20, 40), (25, 36), (30, 36), (28, 42), (23, 40), (19, 42), (15, 44), (10, 48), (5, 52), (0, 50), (-5, 50), (-10, 48), (-10, 42)],
    [(-10, 35), (0, 36), (10, 37), (20, 32), (30, 31), (35, 28), (40, 15), (48, 11), (51, 10), (45, 0), (40, -10), (35, -18), (30, -28), (20, -35), (15, -30), (12, -18), (9, -5), (9, 4), (-8, 5), (-15, 12), (-17, 20), (-15, 28)],
    [(30, 36), (40, 36), (45, 40), (50, 42), (55, 45), (60, 50), (65, 55), (70, 60), (75, 68), (85, 72), (100, 75), (115, 73), (130, 72), (150, 70), (160, 65), (170, 66), (178, 65), (170, 60), (160, 55), (150, 50), (140, 45), (135, 40), (130, 35), (127, 35), (122, 30), (118, 25), (110, 20), (105, 10), (100, 8), (95, 15), (90, 22), (85, 20), (80, 15), (75, 10), (72, 20), (65, 25), (60, 25), (55, 27), (50, 30), (45, 30), (40, 32), (35, 36)],
    [(113, -22), (114, -30), (118, -35), (125, -33), (130, -32), (135, -35), (140, -38), (145, -38), (150, -37), (153, -32), (150, -22), (145, -15), (142, -11), (137, -12), (132, -12), (127, -14), (122, -17), (117, -20)],
    [(-5, 50), (-3, 53), (-5, 56), (-2, 58), (0, 53), (1, 51)],
    [(130, 31), (133, 34), (137, 35), (140, 38), (141, 42), (143, 44), (141, 40), (139, 36)],
]
for poly in CONTINENTS:
    pts = [proj(lon, lat) for lon, lat in poly]
    d.polygon(pts, fill=LAND, outline=LAND_EDGE)

def pin(lon, lat, num, dx=0, dy=0):
    x, y = proj(lon, lat)
    x += dx
    y += dy
    d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=RED, outline=PAPER, width=1)
    t = str(num)
    d.text((x - d.textlength(t, font=f_pin) / 2, y - 5), t, font=f_pin, fill=PAPER)

pin(126.98, 37.57, 23)
pin(116.4, 39.9, 25)
pin(90.4, 23.8, 22)
pin(20.07, 32.12, 15)
pin(34.78, 32.08, 16, dx=-4)
pin(32.53, 15.5, 20)
pin(30.0, 1.7, 21)
pin(30.71, 36.9, 14, dx=6, dy=-4)
pin(2.35, 48.86, 13, dx=-6)
pin(21.01, 52.23, 11, dx=4)
pin(-2.24, 53.48, 27, dx=-4, dy=-4)
pin(-77.04, 38.9, 4)
pin(-74.0, 40.7, 7, dx=8, dy=4)
pin(-59.6, 13.1, 2)
pin(37.62, 55.76, 12, dx=6)
pin(35.5, 33.9, 29, dx=8, dy=2)
pin(50.6, 26.2, 30, dx=4, dy=4)
# callouts
d.text((mx0 + 6, my1 - 34), "WASHINGTON: 04·05·06·10", font=f_meta, fill=INK)
d.text((mx0 + 6, my1 - 22), "SEOUL: 23·24·26   ·   GAZA & W. BANK: 16·17·18",
       font=f_meta, fill=INK)
d.text((mx0 + 6, my1 - 10), "LEGEND: REPORTED = confirmed by its source  ·  CLAIM = one side alleges  ·  DENIAL = disputed  ·  ONGOING = still developing",
       font=f_meta, fill=GRAY)

# right column: numbers + NOT YET
nx0, ny0, nx1 = 656, MY, 1014
d.rectangle([nx0, ny0, nx1, ny0 + 104], fill=LGRAY, outline=INK, width=1)
d.text((nx0 + 8, ny0 + 4), "THE DAY IN NUMBERS", font=f_sec, fill=INK)
nums = [("-3.3%", "Kospi, Monday"), ("5.3", "US–China power gap"),
        ("11,762", "Ebola cases, DRC"), ("10T won", "Seoul rescue fund"),
        ("2%", "billionaire tax plan"), ("$450M", "Skubal's Mets deal")]
for i, (v, lab) in enumerate(nums):
    cx = nx0 + 8 + (i % 3) * 118
    cy = ny0 + 24 + (i // 3) * 40
    d.text((cx, cy), v, font=f_num, fill=RED if i == 0 else INK)
    d.text((cx, cy + 20), lab, font=f_numlab, fill=GRAY)
d.rectangle([nx0, ny0 + 112, nx1, MY + MH], fill=YELLOW_BG, outline=INK, width=1)
d.text((nx0 + 8, ny0 + 116), "NOT YET — DO NOT READ AS DONE", font=f_sec, fill=GOLD)
ny = wrap("Dymer search continues (14 missing)  ·  4 House races uncalled  ·  COP32 venue not set  ·  WHO evacuating trapped Ebola staff",
          f_body, nx1 - nx0 - 16)
ny = trunc(ny, 2)
yy = ny0 + 134
for ln in ny:
    d.text((nx0 + 8, yy), ln, font=f_body, fill=INK)
    yy += 13

# ---------------- story grid ----------------
GY, GB = 484, 952
COLS = [
    ("NORTH AMERICA", 8, [
        ("04", "Bessent demands Nvidia answers", "Treasury chief wants to know who approved China chip sales and how far knowledge of violations went.", "REPORTED", GREEN, "Reuters"),
        ("05", "FBI probes hack of police database", "FBI investigates an apparent hack of the National Crime Information Center used by police nationwide.", "REPORTED", GREEN, "AP"),
        ("06", "Trump: Iran strikes may resume in New Year", "President says he is inclined to resume strikes if no deal is reached with Tehran: 'All they do is talk.'", "ONGOING", BLUE, "NewsNation"),
        ("07", "Nasdaq futures jump 3% as holiday week opens", "Futures rise after Friday's rout; Nasdaq 100 sits near bear market, down ~20% from its record high.", "REPORTED", GREEN, "CNBC"),
        ("08", "Skubal signs $450M Mets deal", "Two-time Cy Young winner agrees a nine-year, $450M contract — the largest deal ever for a pitcher.", "REPORTED", GREEN, "ESPN"),
        ("09", "Tom Jackson dies at 75", "Former Broncos linebacker turned longtime ESPN analyst dies; tributes pour in from the NFL.", "REPORTED", GREEN, "ESPN"),
        ("10", "States sue SpaceX over AI safety claims", "Oregon and Virginia accuse SpaceX of lying about the safety of its generative AI tools.", "REPORTED", GREEN, "Reuters"),
        ("31", "Anthropic IPO: $107.3B, largest ever", "The Claude maker raised a record $107.3B at $83 a share on 19 Nov; debut close $97.17.", "REPORTED", GREEN, "Bloomberg"),
    ]),
    ("EUROPE", 6, [
        ("11", "Poland: 3 Russian missiles crossed our airspace", "Prosecutors confirm three Kh-101 cruise missiles entered Poland on Friday; Tusk calls it a provocation.", "CLAIM", AMBER, "AP"),
        ("12", "Intel warns of Russian nuclear satellite", "Western agencies say Moscow built a satellite to carry a nuclear warhead, launch possible next month.", "CLAIM", AMBER, "Bloomberg"),
        ("13", "Paris, Sat: 100+ back 2% billionaire tax", "Economists, politicians and unions rally behind Zucman's 2% annual minimum wealth tax.", "REPORTED", GREEN, "AFP"),
        ("27", "Manchester: 12,000 cleared after substance scare", "Crowds leave a Manchester event after an unknown substance is dispersed; no casualties reported.", "REPORTED", GREEN, "AP"),
        ("28", "Zelenskyy: 165 Russian missiles in a week", "Kyiv says Moscow fired 165 missiles in seven days as US delays on Patriots frustrate Ukraine.", "REPORTED", GREEN, "Kyiv"),
        ("14", "COP31: the day after", "Sunday's collapse — 194 nations reject the Antalya Pact — draws fury: Guterres 'profoundly frustrated'.", "REPORTED", GREEN, "CNN"),
    ]),
    ("MIDDLE EAST", 6, [
        ("16", "Israel unity talks resume after Sunday stall", "Likud and Eisenkot's Yashar return to the table after coalition talks ended Sunday with no deal.", "ONGOING", BLUE, "Reuters"),
        ("17", "Gaza: two killed in Israeli strike", "Two Palestinians die in a strike on southern Gaza as the ceasefire frays.", "REPORTED", GREEN, "AP"),
        ("18", "West Bank: settler attacks hit villages", "Palestinian villages report fresh settler arson; Eisenkot had called the attacks 'Jewish terrorism'.", "REPORTED", GREEN, "Reuters"),
        ("19", "Iran war: no deal in sight", "Fighting grinds on as Trump says Tehran wants a deal 'but not one acceptable to me'.", "ONGOING", BLUE, "AP"),
        ("29", "Lebanon seizes 264 kg of explosives", "Army says it caught explosives smuggled in from Syria as border smuggling surges.", "REPORTED", GREEN, "Lebanese Army"),
        ("30", "Bahrain, Sat: Iranian strike hits plant, 2 hurt", "A civilian facility is hit and two people injured in Saturday's Iranian attack.", "REPORTED", GREEN, "AP"),
    ]),
    ("AFRICA", 3, [
        ("15", "Benghazi: UN demands probe of port attacks", "UN urges probe after drones hit two Russian ships.", "CLAIM", AMBER, "UN News"),
        ("20", "Sudan: air defences down drones over Khartoum", "Sudan downs drones over Khartoum, witnesses say.", "CLAIM", AMBER, "Reuters"),
        ("21", "DRC: fighting traps Ebola teams", "Ebola teams trapped by fighting in Ituri hospital.", "REPORTED", GREEN, "WHO"),
    ]),
]
# Asia-Pacific appended under Africa column
ASIA = [
    ("22", "Bangladesh: Hasina will be jailed if she returns", "Dhaka vows to jail Hasina if she returns from India.", "REPORTED", GREEN, "Reuters"),
    ("23", "Seoul: minister quits over AI exam chaos", "Minister quits over AI exam-cheating chaos.", "REPORTED", GREEN, "Reuters"),
    ("24", "SK Telecom -7.3% as Anthropic hype cools", "Shares slide as Anthropic IPO glow fades.", "REPORTED", GREEN, "Korea JoongAng"),
    ("25", "China eases margin rules to calm rout", "Beijing cuts margin rules to 80% to calm the rout.", "REPORTED", GREEN, "Morningstar"),
    ("26", "Seoul readies 10T-won stabilisation fund", "Seoul readies a $6.8B fund to steady the Kospi.", "REPORTED", GREEN, "Yonhap"),
]

col_w = 248
col_x = [10, 262, 514, 766]
region_colors = {"NORTH AMERICA": NAVY, "EUROPE": TEAL, "MIDDLE EAST": RED,
                 "AFRICA": AMBER, "ASIA-PACIFIC": (90, 60, 140)}

def draw_story(x, y, num, head, body, tag, tagcol, src, width):
    lines = trunc(wrap(num + "  " + head, f_head, width), 2)
    yy = y
    for ln in lines:
        d.text((x, yy), ln, font=f_head, fill=INK)
        yy += 13
    blines = trunc(wrap(body, f_body, width), 2)
    for ln in blines:
        d.text((x, yy), ln, font=f_body, fill=INK)
        yy += 11
    bw = badge(x, yy + 1, tag, tagcol)
    d.text((x + bw + 5, yy + 2), "· " + src, font=f_meta, fill=GRAY)
    return yy + 13

def draw_header(x, y, name, count):
    d.rectangle([x, y, x + col_w, y + 18], fill=region_colors[name])
    d.text((x + 6, y + 2), name, font=f_kick, fill=PAPER)
    d.text((x + col_w - 20, y + 2), str(count), font=f_kick, fill=PAPER)
    return y + 24

for ci, (region, count, stories) in enumerate(COLS):
    x = col_x[ci]
    y = GY
    y = draw_header(x, y, region, count)
    for s in stories:
        y = draw_story(x, y, *s, col_w)
        y += 2
        if y > GB - 30:
            print("OVERFLOW col", ci, "at story", s[0])
    if ci == 3:
        y = draw_header(x, y + 2, "ASIA-PACIFIC", 5)
        for s in ASIA:
            y = draw_story(x, y, *s, col_w)
            y += 2
            if y > GB - 30:
                print("OVERFLOW col", ci, "at story", s[0])
    print("col", ci, "final y =", y, "limit", GB)

# ---------------- footer ----------------
d.line([10, 958, W - 10, 958], fill=INK, width=1)
d.text((10, 964), "DATE CHECK — Every story dated 23 Nov 2026, unless its kicker says otherwise.  EXCLUDED as not 23 Nov:",
       font=f_small, fill=INK)
d.text((10, 978), "Democrats reach 258 (22 Nov)  ·  Sparta II fire (22 Nov)  ·  El Chapo Isidro captured (22 Nov)  ·  EU–Indonesia pact (21 Nov)  ·  Nigeria boat (21 Nov)  ·  ICJ Myanmar ruling (19 Nov).",
       font=f_small, fill=GRAY)
d.text((10, 992), "REPORTED = confirmed by its source  ·  CLAIM = one side alleges  ·  DENIAL = disputed  ·  ONGOING = still developing.   Sources: AP, Reuters, CNN, BBC, AFP, UN News, WHO, Lowy Institute, Korea JoongAng Daily, Bloomberg.",
       font=f_small, fill=GRAY)
d.text((10, 1006), "THE WORLD TODAY  ·  23 NOV 2026", font=f_small, fill=GRAY)

img.save(OUT, optimize=True)
print("saved", OUT, os.path.getsize(OUT), "bytes,", img.size)
