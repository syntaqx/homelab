"""Generate the README home-network diagram (dark + light) as standalone SVG.

Usage: python3 scripts/network_diagram.py assets
"""
import math, sys, os

W, H = 1800, 1120
MONO = "'IBM Plex Mono', SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "'Space Grotesk', 'Segoe UI', Helvetica, Arial, sans-serif"

THEMES = {
    "dark": dict(bg="#0A1A2B", grid1="rgba(0,209,202,0.045)", grid2="rgba(0,209,202,0.10)",
                 frame="#00D1CA", text="#E4F3F2", muted="#93B4B6", accent="#00D1CA",
                 caution="#F2B33D", room="#5E8790", panel="#0D2236", rack="rgba(0,209,202,0.55)"),
    "light": dict(bg="#F4F8F8", grid1="rgba(0,120,115,0.05)", grid2="rgba(0,120,115,0.11)",
                  frame="#007873", text="#0A1A2B", muted="#4A6670", accent="#007873",
                  caution="#9A5F00", room="#7F9AA0", panel="#FFFFFF", rack="rgba(0,120,115,0.6)"),
}


def build(t):
    o = []
    a = o.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">')
    a('<title id="t">syntaqx home network</title>')
    a('<desc id="d">Floor-plan style map of the home network: GFiber 5 Gig into a GFiber 6E router and a TP-Link '
      'TL-SX1008 10G switch in the basement server room, wired drops to bedrooms and the family room, '
      'Wi-Fi devices in each room, and the darkrock and r630 servers.</desc>')
    a('<defs>'
      f'<pattern id="g1" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="{t["grid1"]}" stroke-width="1"/></pattern>'
      f'<pattern id="g2" width="100" height="100" patternUnits="userSpaceOnUse"><rect width="100" height="100" fill="url(#g1)"/><path d="M100 0H0V100" fill="none" stroke="{t["grid2"]}" stroke-width="1"/></pattern>'
      '</defs>')
    a(f'<rect width="{W}" height="{H}" fill="{t["bg"]}"/>')
    a(f'<rect width="{W}" height="{H}" fill="url(#g2)"/>')
    a(f'<rect x="12" y="12" width="{W-24}" height="{H-24}" fill="none" stroke="{t["frame"]}" stroke-width="2"/>')
    a(f'<rect x="24" y="24" width="{W-48}" height="{H-48}" fill="none" stroke="{t["frame"]}" stroke-opacity="0.45" stroke-width="1"/>')

    def text(x, y, s, size=12, fill=None, anchor="middle", font=MONO, weight=400, ls=0):
        fill = fill or t["text"]
        lsa = f' letter-spacing="{ls}"' if ls else ""
        a(f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{lsa}>{s}</text>')

    def room(x, y, w, h, label, dashed=False, label_top=False):
        da = ' stroke-dasharray="8 6"' if dashed else ""
        a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{t["panel"]}" fill-opacity="0.35" stroke="{t["room"]}" stroke-width="1.5"{da}/>')
        ly = y + 24 if label_top else y + h - 14
        text(x + w - 14, ly, label, 15, t["muted"], "end", SANS, 600, 2)

    def rack(x, y, w, h, label, right=False):
        a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{t["rack"]}" stroke-width="1.25" stroke-dasharray="5 5"/>')
        if right:
            text(x + w - 12, y + 18, label, 11, t["accent"], "end", MONO, 500, 1.5)
        else:
            text(x + 12, y + 18, label, 11, t["accent"], "start", MONO, 500, 1.5)

    def line(pts, color=None, w=2):
        color = color or t["accent"]
        d = "M" + " L".join(f"{x} {y}" for x, y in pts)
        a(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>')

    S = dict(fill=t["panel"], stroke=t["text"])

    def shape(tag, **kw):
        attrs = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in kw.items())
        a(f"<{tag} {attrs}/>")

    def wifi(cx, cy):
        for r in (5, 10, 15):
            x1 = cx - r * math.cos(math.radians(45)); y1 = cy - r * math.sin(math.radians(45))
            x2 = cx + r * math.cos(math.radians(45))
            a(f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 1 {x2:.1f} {y1:.1f}" fill="none" stroke="{t["accent"]}" stroke-width="1.6" stroke-linecap="round"/>')

    def cast(cx, cy, label, wireless=True):
        if wireless: wifi(cx, cy - 20)
        shape("rect", x=cx - 20, y=cy - 13, width=40, height=26, rx=6, fill=S["fill"], stroke=S["stroke"], stroke_width=1.5)
        text(cx, cy + 32, label, 11)

    def monitor(cx, cy, label):
        shape("rect", x=cx - 18, y=cy - 15, width=36, height=24, rx=2, fill=S["fill"], stroke=S["stroke"], stroke_width=1.5)
        line([(cx, cy + 9), (cx, cy + 14)], t["text"], 1.5)
        line([(cx - 16, cy + 15), (cx + 16, cy + 15)], t["text"], 2)
        text(cx, cy + 36, label, 11, weight=600)

    def ap(cx, cy, label):
        shape("circle", cx=cx, cy=cy, r=12, fill=S["fill"], stroke=S["stroke"], stroke_width=1.5)
        shape("circle", cx=cx, cy=cy, r=4.5, fill="none", stroke=t["accent"], stroke_width=1.5)
        text(cx, cy + 32, label, 11)

    def bridge(cx, cy, label1, label2=None):
        shape("rect", x=cx - 18, y=cy - 10, width=36, height=20, rx=4, fill=S["fill"], stroke=S["stroke"], stroke_width=1.5)
        text(cx, cy + 28, label1, 11)
        if label2: text(cx, cy + 42, label2, 11)

    def switch(cx, cy, w, ports):
        shape("rect", x=cx - w / 2, y=cy - 9, width=w, height=18, rx=2, fill=S["fill"], stroke=S["stroke"], stroke_width=1.5)
        gap = (w - 12) / ports
        for i in range(ports):
            px = cx - w / 2 + 6 + i * gap + (gap - 6) / 2
            shape("rect", x=f"{px:.1f}", y=cy - 3, width=6, height=6, fill="none", stroke=t["accent"], stroke_width=1)

    def router(cx, cy):
        for dx in (-18, 0, 18):
            line([(cx + dx, cy - 6), (cx + dx * 1.25, cy - 22)], t["text"], 1.5)
        shape("rect", x=cx - 28, y=cy - 6, width=56, height=12, rx=2, fill=S["fill"], stroke=S["stroke"], stroke_width=1.5)

    def server(cx, cy):
        shape("rect", x=cx - 55, y=cy - 15, width=110, height=30, rx=2, fill=S["fill"], stroke=S["stroke"], stroke_width=1.5)
        shape("rect", x=cx - 44, y=cy - 3, width=44, height=6, fill="none", stroke=t["muted"], stroke_width=1)
        for i in range(5):
            line([(cx + 14 + i * 7, cy - 8), (cx + 14 + i * 7, cy + 8)], t["muted"], 1.5)

    # ---------- header ----------
    text(48, 74, "syntaqx", 32, t["accent"], "start", SANS, 700)
    text(186, 74, "/ home network", 18, t["muted"], "start", MONO)
    text(W - 48, 74, "GFIBER 5 GIG · 10G CORE · REV 2026-11", 12, t["muted"], "end", MONO, 500, 1.5)
    line([(40, 100), (W - 40, 100)], t["frame"], 1)

    # ---------- rooms ----------
    room(40, 130, 400, 420, "GARAGE")
    room(40, 590, 400, 360, "OUTDOORS", dashed=True)
    room(480, 130, 400, 190, "MASTER BEDROOM")
    room(480, 350, 400, 200, "BEDROOM 1")
    room(480, 580, 400, 180, "FAMILY ROOM")
    room(480, 790, 400, 160, "BEDROOM 4")
    room(920, 350, 360, 200, "BEDROOM 2")
    room(1320, 350, 440, 200, "BEDROOM 3")
    room(920, 650, 840, 300, "SERVER ROOM", label_top=True)
    rack(940, 690, 410, 240, "NETWORK RACK · 12U", right=True)
    rack(1370, 690, 370, 240, "SERVER RACK · 15U")

    # ---------- legend ----------
    a(f'<rect x="920" y="130" width="840" height="190" fill="{t["panel"]}" fill-opacity="0.55" stroke="{t["frame"]}" stroke-opacity="0.5" stroke-width="1"/>')
    text(944, 160, "LEGEND", 11, t["accent"], "start", MONO, 600, 2)
    line([(944, 190), (994, 190)]); text(1010, 194, "Wired", 12, anchor="start")
    wifi(969, 230); text(1010, 228, "Wi-Fi", 12, anchor="start")
    a(f'<rect x="944" y="250" width="50" height="22" fill="none" stroke="{t["rack"]}" stroke-dasharray="5 5" stroke-width="1.25"/>')
    text(1010, 266, "Rack", 12, anchor="start")
    text(944, 300, "→ X15", 12, t["caution"], "start", weight=600); text(1010, 300, "Changing soon (see docs/roadmap.md)", 12, anchor="start")
    facts = [("INTERNET", "Google Fiber 5 Gig"), ("CORE", "TP-Link TL-SX1008 · 8× 10G"),
             ("WI-FI", "GFiber 6E router + 2 GFiber 6E APs"), ("SERVERS", "darkrock (Unraid) · r630 (Proxmox, planned)")]
    for i, (k, v) in enumerate(facts):
        y = 194 + i * 34
        text(1300, y, k, 11, t["muted"], "start", MONO, 500, 1.5)
        text(1392, y, v, 12, anchor="start")

    # ---------- wired links (drawn under devices) ----------
    # Family Room: Chromecast -> AP -> lane 906 -> TL-SX1008
    line([(560, 630), (788, 630)])
    line([(812, 630), (906, 630), (906, 870), (972, 870)])
    # Bedroom 4: MAXXI -> lane 894
    line([(558, 845), (894, 845), (894, 876), (972, 876)])
    # Bedroom 2: GUEST -> lane 912
    line([(962, 405), (912, 405), (912, 864), (972, 864)])
    # Bedroom 3: local bus, uplink to TL-SX1008
    line([(1395, 409), (1395, 440)])
    line([(1370, 440), (1660, 440)])
    for x in (1370, 1470, 1565, 1660):
        line([(x, 440), (x, 456 if x in (1370,) else 458)])
    line([(1363, 400), (1340, 400), (1340, 600), (1040, 600), (1040, 861)])
    # Fiber jack -> router, router -> switch, router -> server-rack switch
    line([(1235, 760), (1178, 760)])
    line([(1122, 760), (1060, 760), (1060, 861)])
    line([(1176, 754), (1176, 724), (1460, 724), (1460, 751)])
    # Fiber jack -> internet
    line([(1250, 771), (1250, 1000)])
    # Server rack switch -> servers
    line([(1450, 769), (1450, 845)])
    line([(1470, 769), (1470, 815), (1650, 815), (1650, 845)])

    # ---------- devices ----------
    cast(120, 195, "Chromecast")
    wifi(120, 286)
    shape("rect", x=102, y=298, width=36, height=36, rx=6, fill=S["fill"], stroke=S["stroke"], stroke_width=1.5)
    for gx in (0, 1):
        for gy in (0, 1):
            shape("rect", x=113 + gx * 8, y=304 + gy * 7, width=6, height=5, fill="none", stroke=t["text"], stroke_width=1)
    for gx in range(3):
        shape("rect", x=107 + gx * 10, y=322, width=6, height=6, rx=1, fill="none", stroke=t["text"], stroke_width=1)
    text(120, 352, "myQ", 11); text(120, 366, "Smart Garage", 11)

    wifi(140, 694)
    shape("rect", x=114, y=706, width=34, height=16, rx=2, fill=S["fill"], stroke=S["stroke"], stroke_width=1.5)
    shape("circle", cx=122, cy=714, r=4, fill="none", stroke=t["accent"], stroke_width=1.2)
    line([(148, 714), (162, 714)], t["text"], 1.5)
    line([(162, 702), (162, 734)], t["text"], 2)
    text(140, 760, "Nest Outdoor", 11); text(140, 774, "Camera", 11)
    wifi(320, 684)
    shape("rect", x=307, y=694, width=26, height=44, rx=8, fill=S["fill"], stroke=S["stroke"], stroke_width=1.5)
    shape("circle", cx=320, cy=707, r=6, fill="none", stroke=t["text"], stroke_width=1.2)
    shape("circle", cx=320, cy=725, r=6, fill="none", stroke=t["accent"], stroke_width=1.2)
    text(320, 760, "Nest Doorbell", 11)

    cast(540, 190, "Chromecast")
    cast(540, 410, "Chromecast")
    cast(540, 630, "Chromecast", wireless=False)
    ap(800, 630, "GFiber 6E AP")
    monitor(540, 845, "MAXXI")
    monitor(980, 405, "GUEST")

    # Bedroom 3
    switch(1395, 400, 64, 4)
    text(1436, 404, "2.5G Switch", 11, t["muted"], "start")
    monitor(1370, 473, "SYNTAQX")
    bridge(1470, 470, "Hue Bridge")
    bridge(1565, 470, "SureFlap", "Bridge")
    ap(1660, 470, "GFiber 6E AP")
    cast(1712, 395, "Chromecast")

    # Network rack
    switch(1020, 870, 96, 8)
    text(1020, 902, "TP-Link TL-SX1008", 11, weight=600)
    text(1020, 916, "10G · 8-port", 10, t["muted"])
    router(1150, 760)
    text(1150, 792, "GFiber 6E Router", 11)
    shape("rect", x=1235, y=750, width=30, height=21, rx=3, fill=S["fill"], stroke=S["stroke"], stroke_width=1.5)
    shape("circle", cx=1250, cy=760, r=4, fill="none", stroke=t["accent"], stroke_width=1.2)
    text(1274, 764, "Fiber Jack", 11, anchor="start")

    # Server rack
    switch(1460, 760, 64, 4)
    text(1500, 764, "2.5G Switch", 11, t["muted"], "start")
    server(1460, 860)
    text(1460, 894, "darkrock.local", 11, weight=600)
    text(1460, 910, "→ X15 · Phase 1", 10, t["caution"], weight=600)
    server(1650, 860)
    text(1650, 894, "r630.local", 11, weight=600)
    text(1650, 910, "off until rack UPS", 10, t["muted"])

    # Internet
    a(f'<rect x="1130" y="1000" width="240" height="52" rx="26" fill="{t["panel"]}" stroke="{t["accent"]}" stroke-width="1.5"/>')
    text(1250, 1031, "INTERNET · GFIBER 5 GIG", 12, t["accent"], weight=600, ls=1)

    a("</svg>")
    return "\n".join(o)


out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for name, theme in THEMES.items():
    with open(os.path.join(out, f"network-{name}.svg"), "w") as f:
        f.write(build(theme))
print("ok")
