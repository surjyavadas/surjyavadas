import numpy as np, os
from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageEnhance
from scipy import ndimage as ndi
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist

# ---------------- CONFIG (edit, then re-run) ----------------
CFG = dict(
    user="USERNAME", name="Surjyava Das", role="Full-Stack Developer",
    origin="India", edu="Computer Science", status="Building + Learning + Shipping",
    tool="VS Code, Git, Android Studio, Figma",
    lang="Dart, JavaScript, Python", frontend="Flutter, React, HTML/CSS",
    backend="Node.js, Express", db="Firebase, MongoDB", infra="Vercel, Netlify, GitHub Actions",
    mail="surjyavadas.pro@gmail.com", portfolio="portfolio-surjyavadas.netlify.app",
    linkedin="in/surjyava-das",
)
SRC = "/mnt/user-data/uploads/1791613016472_image.png"
OUT = "/mnt/user-data/outputs"
GW, GH, S = 300, 340, 1.2          # dot grid, svg scale
T, TI = 14.2, 3.2                  # loop length, intro length
rng = np.random.default_rng(7)

# ---------------- portrait ----------------
im = Image.open(SRC).convert("RGB"); W, H = im.size; k = W / 896
crop = im.crop(tuple(int(v * k) for v in (255, 215, 835, 872))).resize((GW, GH), Image.LANCZOS)
a = np.asarray(crop).astype(float)
full = np.asarray(im).astype(float)
sm = ndi.gaussian_filter(a, (1.5, 1.5, 0)); r, g, b = sm[..., 0], sm[..., 1], sm[..., 2]
lum = .3 * r + .59 * g + .11 * b; ratio = g / np.maximum(r, 1)
fg = (lum < 45) | ((ratio > .6) & (ratio < .89) & (lum > 40))   # hair/shirt are dark; skin is warm; wall is grey-olive; sign is saturated red
fg = ndi.binary_opening(fg, iterations=2)
fg = ndi.binary_closing(fg, iterations=4)
fg = ndi.binary_fill_holes(fg)
lab, n = ndi.label(fg)
fg = lab == (np.argmax(ndi.sum(fg, lab, range(1, n + 1))) + 1)
fg = ndi.binary_fill_holes(ndi.binary_closing(fg, iterations=6))
fg = ndi.binary_opening(fg, iterations=4)
lab, n = ndi.label(fg)
fg = lab == (np.argmax(ndi.sum(fg, lab, range(1, n + 1))) + 1)

gray = ImageOps.autocontrast(ImageOps.grayscale(crop), cutoff=1)
gray = ImageEnhance.Contrast(gray).enhance(1.3).filter(ImageFilter.UnsharpMask(radius=3, percent=140))
ga = np.asarray(gray).astype(float)

def fs(f):
    f = f.copy(); h, w = f.shape; out = np.zeros((h, w), bool)
    for y in range(h):
        d = 1 if y % 2 == 0 else -1
        for x in (range(w) if d == 1 else range(w - 1, -1, -1)):
            o = f[y, x]; nw = 255. if o >= 128 else 0.; out[y, x] = nw > 0; e = o - nw
            if 0 <= x + d < w: f[y, x + d] += e * 7 / 16
            if y + 1 < h:
                if 0 <= x - d < w: f[y + 1, x - d] += e * 3 / 16
                f[y + 1, x] += e * 5 / 16
                if 0 <= x + d < w: f[y + 1, x + d] += e / 16
    return out

dk = 255 * (ga / 255) ** .75; dk[~fg] = 0            # lit subject only, bleed cleared at mask edge
DOTS = {"dark": fs(dk) & fg, "light": ~fs(ga)}        # light keeps background, dots = dark parts
np.save(f"{OUT}/dots_dark.npy", DOTS["dark"]); np.save(f"{OUT}/dots_light.npy", DOTS["light"])
np.save(f"{OUT}/mask.npy", fg)

# ---------------- logos -> 900 travellers ----------------
NT = 900
def raster(fn):
    m = Image.new("L", (GW, GH), 0); fn(ImageDraw.Draw(m)); return np.asarray(m) > 0
def flutter(d):
    s = 1.9; ox, oy = 150 - 55 * s, 170 - 50 * s
    for p in ([(50, 0), (100, 0), (36, 64), (11, 38)], [(58, 58), (100, 58), (58, 100), (37, 79)], [(36, 64), (58, 42), (80, 42), (58, 58)]):
        d.polygon([(ox + x * s, oy + y * s) for x, y in p], fill=255)
def code(d):
    d.line([(100, 125), (60, 170), (100, 215)], fill=255, width=16, joint="curve")
    d.line([(200, 125), (240, 170), (200, 215)], fill=255, width=16, joint="curve")
    d.line([(165, 115), (135, 225)], fill=255, width=14)
def vercel(d): d.polygon([(150, 95), (228, 228), (72, 228)], fill=255)
def sample(m):
    ys, xs = np.nonzero(m); i = rng.choice(len(xs), NT, replace=False)
    return np.c_[xs[i] + rng.random(NT), ys[i] + rng.random(NT)]
P1, P2, P3 = (sample(raster(f)) for f in (flutter, code, vercel))
P2 = P2[linear_sum_assignment(cdist(P1, P2))[1]]       # optimal transport = shortest paths
P3 = P3[linear_sum_assignment(cdist(P2, P3))[1]]
c1 = P1.mean(0)

# ---------------- svg ----------------
TH = {
 "dark": dict(bg="#0A101F", win="#0D1526", text="#E2E8F0", dim="#7C8AA5", por="#A78BFA", ch="#22D3EE", ac="#10B981", pillt="#0A101F"),
 "light": dict(bg="#F1F5F9", win="#FFFFFF", text="#0F172A", dim="#64748B", por="#7C3AED", ch="#0891B2", ac="#059669", pillt="#FFFFFF"),
}
esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;")
CW = 8.4
def row(y, label, val, t, hl=False):
    xL, xR = 490, 1140; lw, vw = len(label) * CW, len(val) * CW
    n = int((xR - xL - lw - vw) / CW) - 2
    tl = lambda x, s, w, c, extra="": f'<text x="{x:.1f}" y="{y}" font-size="14" fill="{c}" textLength="{w:.1f}" lengthAdjust="spacingAndGlyphs"{extra}>{esc(s)}</text>'
    return (tl(xL, label, lw, t["ch"]) + tl(xL + lw + CW, "." * n, n * CW, t["dim"], ' opacity=".55"')
            + tl(xR - vw, val, vw, t["ac"] if hl else t["text"]))

def paths(pts):
    return "".join(f"M{x} {y}h0" for x, y in pts)

def build(mode):
    t = TH[mode]; ys, xs = np.nonzero(DOTS[mode]); N = len(xs)
    pts = np.c_[xs, ys]
    # intro: 60 random scattered groups
    gid = rng.integers(0, 60, N); intro = ""; hs = np.zeros((6, 6))
    allh = np.histogram2d(xs, ys, bins=6, range=[[0, GW], [0, GH]])[0]; allh /= allh.sum(); tv = []
    for i in range(60):
        p = pts[gid == i]
        hh = np.histogram2d(p[:, 0], p[:, 1], bins=6, range=[[0, GW], [0, GH]])[0]; tv.append(.5 * np.abs(hh / hh.sum() - allh).sum())
        intro += (f'<path d="{paths(p)}" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{i*.0333:.3f}s" dur="1.2s" fill="freeze"/></path>')
    # loop: ~94 drift bands, per-dot noise (sigma 4) so quantisation doesn't draw a grid
    nx, ny = xs + rng.normal(0, 4, N), ys + rng.normal(0, 4, N)
    band = np.clip((ny / GH * 10).astype(int), 0, 9) * 10 + np.clip((nx / GW * 10).astype(int), 0, 9)
    kt = lambda *v: ";".join(f"{x/T:.4f}" for x in v)
    loop = ""
    for bnd in np.unique(band):
        p = pts[band == bnd]; d = .42 * (c1 - p.mean(0))
        loop += (f'<g><path d="{paths(p)}"/>'
                 f'<animateTransform attributeName="transform" type="translate" begin="{TI}s" dur="{T}s" repeatCount="indefinite" values="0 0;0 0;{d[0]:.1f} {d[1]:.1f};{d[0]:.1f} {d[1]:.1f};0 0" keyTimes="{kt(0,3,4.3,12.9,14.2)}"/>'
                 f'<animate attributeName="opacity" begin="{TI}s" dur="{T}s" repeatCount="indefinite" values="1;1;0;0;1" keyTimes="{kt(0,3,4.3,12.9,14.2)}"/></g>')
    # travellers
    tr = ""
    for a1, a2, a3 in zip(P1, P2, P3):
        d2, d3 = a2 - a1, a3 - a1
        tr += (f'<circle cx="{a1[0]:.1f}" cy="{a1[1]:.1f}" r="1.5"><animateTransform attributeName="transform" type="translate" begin="{TI}s" dur="{T}s" repeatCount="indefinite" '
               f'values="0 0;0 0;{d2[0]:.1f} {d2[1]:.1f};{d2[0]:.1f} {d2[1]:.1f};{d3[0]:.1f} {d3[1]:.1f};{d3[0]:.1f} {d3[1]:.1f}" keyTimes="{kt(0,6.3,7.6,9.6,10.9,14.2)}"/></circle>')
    u = CFG
    rows = [("Subject", u["name"], 0), ("Role", u["role"], 0), ("Origin", u["origin"], 0), ("Education", u["edu"], 0),
            ("Status", u["status"], 1), ("ToolChain", u["tool"], 0), None,
            ("Core.Lang", u["lang"], 0), ("Core.Frontend", u["frontend"], 0), ("Core.Backend", u["backend"], 0),
            ("Core.Database", u["db"], 0), ("Core.Infra", u["infra"], 0), None,
            ("Grid.Mail", u["mail"], 0), ("Grid.Portfolio", u["portfolio"], 0), ("Grid.LinkedIn", u["linkedin"], 0),
            ("Grid.GitHub", "github.com/" + u["user"], 0)]
    y = 132; info = ""
    for r_ in rows:
        if r_ is None: y += 12; continue
        info += row(y, r_[0], r_[1], t, bool(r_[2])); y += 23
    handle = "@" + u["user"]; pw = (len(handle) + 2) * CW
    f = 'font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"'
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="1180" height="610" {f}>
<title>{esc(u["name"])} - profile.sh --live</title>
<rect width="1180" height="610" fill="{t["bg"]}"/>
<rect x="10" y="10" width="1160" height="590" rx="10" fill="{t["win"]}" stroke="{t["ch"]}" stroke-opacity=".6"/>
<path d="M10 46H1170" stroke="{t["ch"]}" stroke-opacity=".3"/>
<circle cx="34" cy="28" r="5.5" fill="#EF4444"/><circle cx="54" cy="28" r="5.5" fill="#F59E0B"/><circle cx="74" cy="28" r="5.5" fill="{t["ac"]}"/>
<text x="590" y="33" font-size="13" fill="{t["dim"]}" text-anchor="middle">profile.sh --live</text>
<rect x="34" y="64" width="412" height="520" fill="none" stroke="{t["ch"]}" stroke-opacity=".5"/>
<text x="46" y="84" font-size="13" fill="{t["ch"]}">VISUAL.MAP</text>
<text x="434" y="84" font-size="11" fill="{t["dim"]}" text-anchor="end">1-bit / fs-serpentine</text>
<g transform="translate(60.6,120.6) scale({S})" fill="none" stroke="{t["por"]}" stroke-width="1" stroke-linecap="square" shape-rendering="crispEdges">
<g opacity="1">{intro}<set attributeName="opacity" to="0" begin="{TI}s" fill="freeze"/></g>
<g opacity="0">{loop}<set attributeName="opacity" to="1" begin="{TI}s" fill="freeze"/></g>
<g fill="{t["por"]}" stroke="none" shape-rendering="geometricPrecision" opacity="0">{tr}
<set attributeName="opacity" to="1" begin="{TI}s" fill="freeze"/>
<animate attributeName="opacity" begin="{TI}s" dur="{T}s" repeatCount="indefinite" values="0;0;1;1;0" keyTimes="{kt(0,3,4.3,12.9,14.2)}"/></g>
</g>
<text x="490" y="84" font-size="13" fill="{t["ch"]}" letter-spacing="1">SYSTEM.INFO</text>
<circle cx="618" cy="79" r="4" fill="#EF4444"><animate attributeName="opacity" values="1;.25;1" dur="1.4s" repeatCount="indefinite"/></circle>
<text x="628" y="84" font-size="12" fill="#EF4444" font-weight="bold">LIVE</text>
<rect x="{1140-pw:.1f}" y="66" width="{pw:.1f}" height="24" rx="12" fill="{t["ch"]}"/>
<text x="{1140-pw/2:.1f}" y="83" font-size="14" font-weight="bold" fill="{t["pillt"]}" text-anchor="middle" textLength="{len(handle)*CW:.1f}" lengthAdjust="spacingAndGlyphs">{esc(handle)}</text>
<path d="M490 100H1140" stroke="{t["ch"]}" stroke-opacity=".3" stroke-dasharray="2 4"/>
{info}
<text x="490" y="560" font-size="14" fill="{t["ac"]}">visitor@github:~$</text>
<rect x="640" y="548" width="9" height="16" fill="{t["ac"]}"><animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/></rect>
</svg>'''
    open(f"{OUT}/{mode}.svg", "w").write(svg)
    return N, np.mean(tv), len(svg) / 1024, len(np.unique(band))

for m in ("dark", "light"):
    N, tv, kb, nb = build(m)
    print(f"{m}: dots={N} bands={nb} evenness(TVD)={tv:.3f} size={kb:.0f}KB")

# preview for the mask / dither check (raster of first frame)
pv = Image.new("RGB", (GW * 3, GH), "#0A101F")
pv.paste(crop, (0, 0)); pv.paste(Image.fromarray((fg * 255).astype("uint8")).convert("RGB"), (GW, 0))
dd = np.zeros((GH, GW, 3), "uint8"); dd[DOTS["dark"]] = (167, 139, 250); pv.paste(Image.fromarray(dd), (2 * GW, 0))
pv.save("/home/claude/preview.png")
