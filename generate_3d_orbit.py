#!/usr/bin/env python3
"""
Generate 3d-orbit.svg: a self-contained, animated 3D scene for a GitHub profile README.

- A rotating wireframe icosahedron (true 3D rotation + perspective projection)
- Two tilted orbit rings with tech labels travelling around them in 3D
  (labels shrink/fade as they pass behind the core -> real depth cue)
- A slow twinkling starfield

All 3D math is done here in Python and baked into SMIL keyframes, so the output
is a plain SVG (no JavaScript) that GitHub renders inside <img>/<picture>.

Usage:  python3 generate_3d_orbit.py [output.svg]
"""
import math
import random
import sys

W, H = 900, 420
CX, CY = W / 2, H / 2 - 4
DUR = 18            # seconds per loop
FRAMES = 72         # keyframes per loop
FOCAL = 900         # perspective focal length

CYAN, VIOLET, INDIGO, TEXT = "#22D3EE", "#A78BFA", "#312E81", "#E2E8F0"


# ---------- tiny 3D helpers ----------
def rot_x(p, a):
    x, y, z = p
    c, s = math.cos(a), math.sin(a)
    return (x, y * c - z * s, y * s + z * c)


def rot_y(p, a):
    x, y, z = p
    c, s = math.cos(a), math.sin(a)
    return (x * c + z * s, y, -x * s + z * c)


def rot_z(p, a):
    x, y, z = p
    c, s = math.cos(a), math.sin(a)
    return (x * c - y * s, x * s + y * c, z)


def project(p):
    """Perspective projection. +z is away from the viewer.
    Returns (screen_x, screen_y, scale, z)."""
    x, y, z = p
    k = FOCAL / (FOCAL + z)
    return CX + x * k, CY + y * k, k, z


def f(v, nd=1):
    s = f"{v:.{nd}f}"
    return s.rstrip("0").rstrip(".") if "." in s else s


def values(seq, nd=1):
    return ";".join(f(v, nd) for v in seq)


def anim(attr, seq, nd=1):
    return (f'<animate attributeName="{attr}" dur="{DUR}s" repeatCount="indefinite" '
            f'values="{values(seq, nd)}"/>')


# ---------- icosahedron ----------
PHI = (1 + 5 ** 0.5) / 2
RAW = [(-1, PHI, 0), (1, PHI, 0), (-1, -PHI, 0), (1, -PHI, 0),
       (0, -1, PHI), (0, 1, PHI), (0, -1, -PHI), (0, 1, -PHI),
       (PHI, 0, -1), (PHI, 0, 1), (-PHI, 0, -1), (-PHI, 0, 1)]
R_CORE = 82
VERTS = [tuple(c * R_CORE / math.sqrt(1 + PHI ** 2) for c in v) for v in RAW]
# edges = vertex pairs at the minimum distance
_d = lambda a, b: math.dist(VERTS[a], VERTS[b])
_min = min(_d(i, j) for i in range(12) for j in range(i + 1, 12))
EDGES = [(i, j) for i in range(12) for j in range(i + 1, 12)
         if abs(_d(i, j) - _min) < 1e-6]
assert len(EDGES) == 30


def core_pose(t):
    """Pose of the core at loop phase t in [0, 1]. Integer turns => seamless loop."""
    ry = 2 * math.pi * 2 * t       # 2 turns about Y
    rx = 2 * math.pi * 1 * t + 0.5  # 1 turn about X (with a fixed tilt)
    rz = 2 * math.pi * 1 * t       # 1 turn about Z
    def pose(v):
        return rot_z(rot_x(rot_y(v, ry), rx), rz)
    return pose


# ---------- orbit rings ----------
RINGS = [
    # radius, tilt about X, tilt about Z, direction, labels, colour
    dict(r=150, tx=1.05, tz=-0.30, dir=1, color=CYAN,
         labels=["Python", "C / C++", "JavaScript", "SQL"]),
    dict(r=205, tx=0.6, tz=0.28, dir=-1, color=VIOLET,
         labels=["React", "Node.js", "AI / ML", "Git"]),
]


def ring_point(ring, ang):
    p = (ring["r"] * math.cos(ang), 0.0, ring["r"] * math.sin(ang))
    return rot_z(rot_x(p, ring["tx"]), ring["tz"])


def depth_factor(z, zmax):
    """0 (far/back) .. 1 (near/front)."""
    return max(0.0, min(1.0, (zmax - z) / (2 * zmax)))


# ---------- build svg ----------
def build():
    out = []
    a = out.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      f'role="img" aria-label="Animated 3D scene: a rotating wireframe core with tech stack labels orbiting it">')
    a('<defs>')
    a(f'<radialGradient id="bg" cx="50%" cy="50%" r="70%">'
      f'<stop offset="0" stop-color="#111a33"/><stop offset="1" stop-color="#0A101F"/></radialGradient>')
    a(f'<radialGradient id="glow" cx="50%" cy="50%" r="50%">'
      f'<stop offset="0" stop-color="{CYAN}" stop-opacity=".55"/>'
      f'<stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>')
    a(f'<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">'
      f'<stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{VIOLET}"/></linearGradient>')
    a('</defs>')
    a(f'<rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/>')
    a(f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="16" fill="none" stroke="{CYAN}" stroke-opacity=".35"/>')

    # starfield (deterministic)
    rnd = random.Random(7)
    for i in range(70):
        x, y = rnd.uniform(10, W - 10), rnd.uniform(10, H - 10)
        r = rnd.choice([0.7, 0.9, 1.2, 1.5])
        d = rnd.uniform(3, 7)
        begin = -rnd.uniform(0, d)
        a(f'<circle cx="{f(x)}" cy="{f(y)}" r="{r}" fill="{TEXT}" opacity=".5">'
          f'<animate attributeName="opacity" values=".15;.9;.15" dur="{f(d, 2)}s" begin="{f(begin, 2)}s" repeatCount="indefinite"/></circle>')

    # static orbit rings (projected polylines)
    for ring in RINGS:
        pts = []
        for i in range(97):
            ang = 2 * math.pi * i / 96
            sx, sy, _, _ = project(ring_point(ring, ang))
            pts.append(f"{f(sx)},{f(sy)}")
        a(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{ring["color"]}" '
          f'stroke-opacity=".28" stroke-width="1" stroke-dasharray="3 6"/>')

    # glow behind core
    a(f'<circle cx="{f(CX)}" cy="{f(CY)}" r="120" fill="url(#glow)">'
      f'<animate attributeName="r" values="112;128;112" dur="4.5s" repeatCount="indefinite"/></circle>')

    # --- items that need depth sorting are split into "back" and "front" groups ---
    # Labels behind the core are drawn first, labels in front are drawn last.
    # Because depth changes over time we render each label twice: once in the back
    # layer (visible only while z > 0) and once in the front layer (while z <= 0).
    label_back, label_front = [], []
    zmax = max(r["r"] for r in RINGS)

    n_per_ring = {i: len(r["labels"]) for i, r in enumerate(RINGS)}
    for ri, ring in enumerate(RINGS):
        n = n_per_ring[ri]
        for li, text in enumerate(ring["labels"]):
            base = 2 * math.pi * li / n + ri * 0.7
            xs, ys, fs, op_back, op_front, = [], [], [], [], []
            for k in range(FRAMES + 1):
                t = k / FRAMES
                ang = base + ring["dir"] * 2 * math.pi * t
                sx, sy, sc, z = project(ring_point(ring, ang))
                xs.append(sx)
                ys.append(sy)
                fs.append(15 * sc)
                near = depth_factor(z, zmax)
                vis = 0.35 + 0.65 * near
                # hard split at z = 0 with a short fade to avoid popping
                in_front = max(0.0, min(1.0, (-z + 14) / 28))
                op_front.append(vis * in_front)
                op_back.append(vis * (1 - in_front) * 0.85)
            for bucket, ops in ((label_back, op_back), (label_front, op_front)):
                bucket.append(
                    f'<g font-family="JetBrains Mono, Consolas, monospace" font-weight="700" '
                    f'text-anchor="middle" fill="{ring["color"]}">'
                    f'<text>{text}'
                    f'{anim("x", xs)}{anim("y", ys)}{anim("font-size", fs)}{anim("opacity", ops, 2)}'
                    f'</text></g>')
                # a small dot that rides with the label
            dot_x = [x for x in xs]
            dot_y = [y + 9 for y in ys]
    a("<!-- labels behind core -->")
    out.extend(label_back)

    # wireframe core
    verts_t = []
    for k in range(FRAMES + 1):
        pose = core_pose(k / FRAMES)
        verts_t.append([project(pose(v)) for v in VERTS])

    for (i, j) in EDGES:
        x1 = [verts_t[k][i][0] for k in range(FRAMES + 1)]
        y1 = [verts_t[k][i][1] for k in range(FRAMES + 1)]
        x2 = [verts_t[k][j][0] for k in range(FRAMES + 1)]
        y2 = [verts_t[k][j][1] for k in range(FRAMES + 1)]
        zm = [(verts_t[k][i][3] + verts_t[k][j][3]) / 2 for k in range(FRAMES + 1)]
        op = [0.25 + 0.75 * depth_factor(z, R_CORE) for z in zm]
        a(f'<line stroke="url(#edge)" stroke-width="1.6" stroke-linecap="round" '
          f'x1="{f(x1[0])}" y1="{f(y1[0])}" x2="{f(x2[0])}" y2="{f(y2[0])}">'
          f'{anim("x1", x1)}{anim("y1", y1)}{anim("x2", x2)}{anim("y2", y2)}{anim("opacity", op, 2)}</line>')
    for v in range(12):
        xs = [verts_t[k][v][0] for k in range(FRAMES + 1)]
        ys = [verts_t[k][v][1] for k in range(FRAMES + 1)]
        rs = [2.2 * verts_t[k][v][2] for k in range(FRAMES + 1)]
        op = [0.4 + 0.6 * depth_factor(verts_t[k][v][3], R_CORE) for k in range(FRAMES + 1)]
        a(f'<circle fill="{TEXT}" cx="{f(xs[0])}" cy="{f(ys[0])}" r="{f(rs[0], 2)}">'
          f'{anim("cx", xs)}{anim("cy", ys)}{anim("r", rs, 2)}{anim("opacity", op, 2)}</circle>')

    # bright core
    a(f'<circle cx="{f(CX)}" cy="{f(CY)}" r="5" fill="{TEXT}">'
      f'<animate attributeName="r" values="4;7;4" dur="2.4s" repeatCount="indefinite"/></circle>')

    a("<!-- labels in front of core -->")
    out.extend(label_front)

    # caption
    a(f'<text x="{f(CX)}" y="{H - 16}" text-anchor="middle" font-family="JetBrains Mono, Consolas, monospace" '
      f'font-size="11" fill="{TEXT}" opacity=".55" letter-spacing="3">// SURJYAVA.DAS &#183; STACK IN ORBIT</text>')
    a('</svg>')
    return "\n".join(out)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "3d-orbit.svg"
    svg = build()
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print(f"wrote {path} ({len(svg) / 1024:.0f} KB)")
