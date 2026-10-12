"""NetWork / NX35 website loops — 3D, white background, no text/logo. 1920x1080, 10 s, seamless.
Each scene is a deterministic Three.js render driven by HyperFrames time (hf-seek)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
W, H, D = 1920, 1080, 10

HTML = """<!doctype html>
<html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width={W}, height={H}" />
<title>{title}</title>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
  html, body {{ margin: 0; background: #fff; }}
  #root {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; }}
  #bg {{ position: absolute; inset: 0; background: #ffffff; }}
  #three-layer {{ position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; display: block; }}
</style></head><body>
<div id="root" data-composition-id="main" data-width="{W}" data-height="{H}" data-duration="{D}">
  <div id="bg"></div>
  <canvas id="three-layer" width="{W}" height="{H}"></canvas>
</div>
<script>
  window.__timelines = window.__timelines || {{}};
  const tl = gsap.timeline({{ paused: true }});
  tl.to("#bg", {{ opacity: 1, duration: {D} }}, 0);
  window.__timelines["main"] = tl;
</script>
<script type="module">
  import * as THREE from "https://cdn.jsdelivr.net/npm/three@0.181.2/+esm";
  const W = {W}, H = {H}, D = {D}, TAU = Math.PI * 2;
  function rng(seed) {{ return function () {{ seed |= 0; seed = (seed + 0x6D2B79F5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }}; }}
  const canvas = document.getElementById("three-layer");
  const renderer = new THREE.WebGLRenderer({{ canvas, antialias: true, alpha: false, preserveDrawingBuffer: true }});
  renderer.setSize(W, H, false); renderer.setPixelRatio(1);
  renderer.setClearColor(0xffffff, 1);
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  const scene = new THREE.Scene(); scene.background = new THREE.Color(0xffffff);
  const pmrem = new THREE.PMREMGenerator(renderer);
  // simple bright studio env for reflections
  const envScene = new THREE.Scene(); envScene.background = new THREE.Color(0xffffff);
  const envLight = new THREE.Mesh(new THREE.SphereGeometry(10, 32, 16), new THREE.MeshBasicMaterial({{ color: 0xf6eef8, side: THREE.BackSide }}));
  envScene.add(envLight);
  const pane = new THREE.Mesh(new THREE.PlaneGeometry(6, 6), new THREE.MeshBasicMaterial({{ color: 0xffffff }})); pane.position.set(0, 6, 4); pane.lookAt(0, 0, 0); envScene.add(pane);
  scene.environment = pmrem.fromScene(envScene, 0.04).texture;
  scene.add(new THREE.HemisphereLight(0xffffff, 0xf1e4f4, 1.4));
  const key = new THREE.DirectionalLight(0xffffff, 2.2); key.position.set(5, 8, 7); scene.add(key);
  const rim = new THREE.DirectionalLight(0xf6c9ff, 1.4); rim.position.set(-7, -2, -6); scene.add(rim);
{scene}
  window.addEventListener("hf-seek", (e) => renderAt(e.detail.time));
  renderAt(window.__hfThreeTime || 0);
</script></body></html>
"""

VESICLE = """
  function makeVesicle(r, rand, tint) {
    const g = new THREE.Group();
    const shell = new THREE.Mesh(new THREE.SphereGeometry(r, 48, 32), new THREE.MeshPhysicalMaterial({ color: tint || 0xefc2f4, roughness: 0.12, transmission: 0.4, thickness: r * 0.8, ior: 1.35, clearcoat: 1, clearcoatRoughness: 0.08, transparent: true, opacity: 0.92, sheen: 0.6, sheenColor: new THREE.Color(0xffe6ff) }));
    const inner = new THREE.Mesh(new THREE.SphereGeometry(r * 0.8, 32, 24), new THREE.MeshStandardMaterial({ color: 0xd987e6, roughness: 0.4, transparent: true, opacity: 0.6 }));
    g.add(shell, inner);
    const n = 10 + Math.floor(rand() * 8);
    const pg = new THREE.SphereGeometry(r * 0.09, 12, 8), pm = new THREE.MeshStandardMaterial({ color: 0xa921c0, roughness: 0.35, metalness: 0.05 });
    for (let i = 0; i < n; i++) {
      const u = rand() * 2 - 1, th = rand() * TAU, s = Math.sqrt(1 - u * u);
      const p = new THREE.Mesh(pg, pm); p.position.set(r * s * Math.cos(th), r * u, r * s * Math.sin(th)); g.add(p);
    }
    return g;
  }
"""

SCENES = {}

# A — exosome field
SCENES["A-exosome-field"] = ("Exosome field", VESICLE + """
  scene.fog = new THREE.Fog(0xffffff, 10, 30);
  const camera = new THREE.PerspectiveCamera(32, W / H, 0.1, 100);
  const rand = rng(7); const items = [];
  for (let i = 0; i < 64; i++) {
    const r = 0.25 + Math.pow(rand(), 2) * 0.9;
    const v = makeVesicle(r, rand, i % 9 === 0 ? 0xf7d6da : 0xf3cff6);
    const z = -rand() * 20 + 4; const sp = (14 - z) * 0.55; const base = new THREE.Vector3((rand() - 0.5) * sp * 1.9, (rand() - 0.5) * sp * 1.05, z);
    items.push({ v, base, a: new THREE.Vector3(0.4 + rand() * 0.9, 0.3 + rand() * 0.8, 0.3 + rand() * 0.6), ph: rand() * TAU, k: 1 + Math.floor(rand() * 2), spin: (rand() - 0.5) * 2 });
    scene.add(v);
  }
  function renderAt(t) {
    const p = (t / D) * TAU;
    for (const it of items) {
      it.v.position.set(it.base.x + Math.sin(p * it.k + it.ph) * it.a.x, it.base.y + Math.cos(p * it.k + it.ph * 1.3) * it.a.y, it.base.z + Math.sin(p + it.ph * 0.7) * it.a.z);
      it.v.rotation.set(Math.sin(p + it.ph) * 0.4, p * Math.round(it.spin + 0.5 * Math.sign(it.spin)), 0);
    }
    camera.position.set(Math.sin(p) * 0.8, Math.cos(p) * 0.4, 14 + Math.sin(p) * 0.6);
    camera.lookAt(0, 0, 0);
    renderer.render(scene, camera);
  }
""")

# B — exosomes signal a cell
SCENES["B-signal-to-cell"] = ("Exosomes signal a cell", VESICLE + """
  const camera = new THREE.PerspectiveCamera(30, W / H, 0.1, 100);
  const rand = rng(11);
  const cellC = new THREE.Vector3(3.2, 0, 0);
  const cg = new THREE.IcosahedronGeometry(3.3, 64); const pos = cg.attributes.position; const vv = new THREE.Vector3();
  for (let i = 0; i < pos.count; i++) { vv.fromBufferAttribute(pos, i); const n = Math.sin(vv.x * 1.7) * Math.sin(vv.y * 2.1 + 1) * Math.sin(vv.z * 1.3 + 2); vv.multiplyScalar(1 + n * 0.06); pos.setXYZ(i, vv.x, vv.y, vv.z); }
  cg.computeVertexNormals();
  const cell = new THREE.Mesh(cg, new THREE.MeshPhysicalMaterial({ color: 0xe8c3f0, roughness: 0.3, transmission: 0.25, thickness: 2.5, ior: 1.33, clearcoat: 0.8, sheen: 0.8, sheenColor: new THREE.Color(0xffffff), transparent: true, opacity: 0.7, depthWrite: false }));
  cell.position.copy(cellC); scene.add(cell);
  const nucMat = new THREE.MeshStandardMaterial({ color: 0x9a2fc0, roughness: 0.45, emissive: 0xa921c0, emissiveIntensity: 0.1 });
  const nuc = new THREE.Mesh(new THREE.IcosahedronGeometry(1.25, 32), nucMat); nuc.position.copy(cellC); scene.add(nuc);
  const hc = document.createElement('canvas'); hc.width = hc.height = 256; const hx = hc.getContext('2d'); const gr = hx.createRadialGradient(128,128,0,128,128,128); gr.addColorStop(0,'rgba(214,80,235,1)'); gr.addColorStop(0.5,'rgba(214,80,235,0.35)'); gr.addColorStop(1,'rgba(214,80,235,0)'); hx.fillStyle = gr; hx.fillRect(0,0,256,256);
  const halo = new THREE.Sprite(new THREE.SpriteMaterial({ map: new THREE.CanvasTexture(hc), transparent: true, opacity: 0, depthTest: false })); halo.renderOrder = 9; halo.scale.set(4.2, 4.2, 1); halo.position.copy(cellC); scene.add(halo);
  const hb = halo.scale.clone(); const _hs = halo.scale.setScalar.bind(halo.scale); halo.scale.setScalar = (k) => halo.scale.set(hb.x * k, hb.y * k, 1);
  const N = 7, ex = [], parts = [];
  const pg = new THREE.SphereGeometry(0.11, 14, 10);
  for (let i = 0; i < N; i++) {
    const v = makeVesicle(0.62, rand); scene.add(v);
    const ang = (i / N) * TAU * 0.55 - 0.85;
    const target = cellC.clone().add(new THREE.Vector3(-Math.cos(ang) * 3.25, Math.sin(ang) * 3.25 * 0.95, Math.sin(i) * 0.6));
    const start = new THREE.Vector3(-10 - rand() * 2, (rand() - 0.5) * 7, (rand() - 0.5) * 4);
    const ps = [];
    for (let k = 0; k < 9; k++) { const m = new THREE.Mesh(pg, new THREE.MeshBasicMaterial({ color: 0xc21fd6, transparent: true, depthTest: false })); m.renderOrder = 10; scene.add(m); ps.push({ m, j: new THREE.Vector3((rand() - 0.5) * 0.8, (rand() - 0.5) * 0.8, (rand() - 0.5) * 0.8), d: rand() * 0.08 }); }
    ex.push({ v, target, start, off: i / N, ps });
  }
  const ease = (x) => x < 0.5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2;
  function renderAt(t) {
    const p = (t / D) * TAU; let glow = 0;
    for (const e of ex) {
      const u = ((t / D) * 2 + e.off) % 1; // each exosome cycles twice per loop
      if (u < 0.55) { const s = ease(u / 0.55); e.v.position.lerpVectors(e.start, e.target, s); e.v.scale.setScalar(1); e.v.visible = true; }
      else if (u < 0.68) { const s = (u - 0.55) / 0.13; e.v.position.copy(e.target).lerp(cellC, s * 0.08); e.v.scale.setScalar(1 - s); e.v.visible = s < 0.99; }
      else { e.v.visible = false; }
      e.v.rotation.y = p * 2;
      for (const q of e.ps) {
        const w = (u - 0.6 - q.d) / 0.32;
        if (w > 0 && w < 1) {
          const a = e.target.clone().add(q.j); const b = cellC.clone().add(q.j.clone().multiplyScalar(0.4));
          q.m.position.lerpVectors(a, b, ease(w)); q.m.visible = true; q.m.material.opacity = Math.min(1, w * 5) * (1 - Math.max(0, (w - 0.85) / 0.15));
          if (w > 0.8) glow += (w - 0.8) * 0.6;
        } else q.m.visible = false;
      }
    }
    nucMat.emissiveIntensity = 0.15 + Math.min(1.6, glow * 1.4);
    nuc.scale.setScalar(1 + Math.min(0.08, glow * 0.06));
    halo.material.opacity = Math.min(0.55, glow * 0.5); halo.scale.setScalar(1 + Math.min(0.5, glow * 0.4));
    cell.rotation.y = p; cell.rotation.x = Math.sin(p) * 0.08;
    camera.position.set(Math.sin(p) * 1.0, 1.0 + Math.cos(p) * 0.4, 14);
    camera.lookAt(0.6, 0, 0);
    renderer.render(scene, camera);
  }
""")

# C — collagen triple helix
SCENES["C-collagen-helix"] = ("Collagen triple helix", """
  scene.fog = new THREE.Fog(0xffffff, 12, 34);
  const camera = new THREE.PerspectiveCamera(30, W / H, 0.1, 100);
  const rand = rng(5);
  const group = new THREE.Group(); scene.add(group);
  const mats = [0xf4d2f7, 0xe7a4ef, 0xd6141f].map((c, i) => new THREE.MeshPhysicalMaterial({ color: c, roughness: 0.22, clearcoat: 1, clearcoatRoughness: 0.1, sheen: 0.5, sheenColor: new THREE.Color(0xffffff), transmission: i === 2 ? 0 : 0.15, thickness: 0.4 }));
  function helix(L, R, turns, phase) {
    class C extends THREE.Curve { getPoint(u) { const a = u * TAU * turns + phase; return new THREE.Vector3(R * Math.cos(a), (u - 0.5) * L, R * Math.sin(a)); } }
    return new C();
  }
  function triple(L, scale) {
    const g = new THREE.Group();
    for (let s = 0; s < 3; s++) g.add(new THREE.Mesh(new THREE.TubeGeometry(helix(L, 0.28 * scale, L / (2.2 * scale), s * TAU / 3), 600, 0.16 * scale, 16, false), mats[s === 2 ? (rand() < 0.35 ? 2 : 1) : s]));
    return g;
  }
  const hero = triple(26, 1.6); group.add(hero);
  const bundle = [];
  for (let i = 0; i < 14; i++) {
    const tr = triple(30, 0.7 + rand() * 0.4); const a = rand() * TAU, d = 3.2 + rand() * 4;
    tr.position.set(Math.cos(a) * d, (rand() - 0.5) * 4, Math.sin(a) * d - 2); tr.rotation.y = rand() * TAU; group.add(tr); bundle.push({ tr, a, d, ph: rand() * TAU });
  }
  group.rotation.z = 0.5;
  function renderAt(t) {
    const p = (t / D) * TAU;
    hero.rotation.y = p; for (const b of bundle) { b.tr.rotation.y = p + b.ph; b.tr.position.y = Math.sin(p + b.ph) * 0.6; }
    group.rotation.y = Math.sin(p) * 0.15;
    camera.position.set(Math.sin(p) * 1.5, 1.0, 15 + Math.cos(p) * 0.8); camera.lookAt(0, 0, 0);
    renderer.render(scene, camera);
  }
""")

# D — scratch assay: cells migrate and close the gap
SCENES["D-cell-migration"] = ("Cell migration", """
  const camera = new THREE.PerspectiveCamera(28, W / H, 0.1, 100);
  const rand = rng(3);
  const cols = 46, rows = 26, sx = 0.62, sy = 0.62;
  const cells = [];
  for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) {
    const x = (c - cols / 2) * sx + (r % 2) * sx * 0.5 + (rand() - 0.5) * 0.25, y = (r - rows / 2) * sy + (rand() - 0.5) * 0.25;
    cells.push({ x, y, s: 0.75 + rand() * 0.45, rot: rand() * TAU, ph: rand() * TAU, e: 0.65 + rand() * 0.35 });
  }
  const geo = new THREE.SphereGeometry(0.34, 20, 14);
  const body = new THREE.InstancedMesh(geo, new THREE.MeshPhysicalMaterial({ color: 0xe6b0ee, roughness: 0.35, clearcoat: 0.6, transmission: 0.1, thickness: 0.3 }), cells.length);
  const nucl = new THREE.InstancedMesh(new THREE.SphereGeometry(0.12, 16, 12), new THREE.MeshStandardMaterial({ color: 0x8e1aa6, roughness: 0.4 }), cells.length);
  scene.add(body, nucl);
  const m = new THREE.Matrix4(), q = new THREE.Quaternion(), sc = new THREE.Vector3(), ps = new THREE.Vector3(), eu = new THREE.Euler();
  const GAP = 3.4;
  function renderAt(t) {
    const p = (t / D) * TAU; const close = 0.5 - 0.5 * Math.cos(p); // 0 open -> 1 closed -> 0
    cells.forEach((c, i) => {
      const open = Math.sign(c.x || 1) * (Math.abs(c.x) * (1 - GAP / (cols * sx)) + GAP / 2);
      const k = Math.min(1, close * (0.6 + 0.6 * Math.exp(-Math.abs(c.x) / 4)));
      const x = open + (c.x - open) * k + Math.sin(p * 2 + c.ph) * 0.03, y = c.y + Math.cos(p * 2 + c.ph) * 0.03;
      const moving = (1 - Math.abs(Math.cos(p))) * Math.exp(-Math.abs(c.x) / 3);
      eu.set(0, 0, c.rot + Math.sin(p + c.ph) * 0.3); q.setFromEuler(eu);
      sc.set(c.s * (1.25 + moving * 0.5), c.s * c.e, 0.32); ps.set(x, y, 0); m.compose(ps, q, sc); body.setMatrixAt(i, m);
      sc.set(c.s, c.s * 0.9, 0.6); ps.set(x, y, 0.08); m.compose(ps, q, sc); nucl.setMatrixAt(i, m);
    });
    body.instanceMatrix.needsUpdate = true; nucl.instanceMatrix.needsUpdate = true;
    camera.position.set(Math.sin(p) * 0.6, -9 + Math.cos(p) * 0.3, 19); camera.lookAt(0, 0, 0);
    renderer.render(scene, camera);
  }
""")

# E — fluorescence: collagen network intensifies around cells
SCENES["E-fluorescence-collagen"] = ("Collagen fluorescence", """
  const camera = new THREE.PerspectiveCamera(30, W / H, 0.1, 100);
  const rand = rng(21);
  const fibMat = new THREE.MeshStandardMaterial({ color: 0xe8334a, emissive: 0xd6141f, emissiveIntensity: 0.4, roughness: 0.5, transparent: true, opacity: 0.2 });
  const cytMat = new THREE.MeshPhysicalMaterial({ color: 0xf7e2ea, roughness: 0.4, transmission: 0.3, thickness: 0.5, transparent: true, opacity: 0.9 });
  const nucMat = new THREE.MeshStandardMaterial({ color: 0x6b6cf0, roughness: 0.45, emissive: 0x3b3cc8, emissiveIntensity: 0.15 });
  const group = new THREE.Group(); scene.add(group); const cells = [];
  for (let i = 0; i < 22; i++) {
    const c = new THREE.Group(); const x = (rand() - 0.5) * 22, y = (rand() - 0.5) * 12;
    const cyt = new THREE.Mesh(new THREE.SphereGeometry(1, 32, 20), cytMat); cyt.scale.set(1.4 + rand(), 0.9 + rand() * 0.6, 0.35); c.add(cyt);
    const nu = new THREE.Mesh(new THREE.SphereGeometry(0.45, 24, 16), nucMat); nu.scale.set(1.2, 1, 0.8); nu.position.z = 0.15; c.add(nu);
    const sx = cyt.scale.x, sy = cyt.scale.y;
    for (let f = 0; f < 9; f++) {
      const off = (rand() - 0.5) * sy * 1.3, half = Math.sqrt(Math.max(0.05, 1 - Math.pow(off / sy, 2))) * sx * 0.88, pts = [];
      for (let k = 0; k <= 8; k++) { const u = k / 8 - 0.5; pts.push(new THREE.Vector3(u * half * 2, off * (1 - 1.2 * u * u) + Math.sin(u * 6 + f) * 0.04, 0.3 + (rand() - 0.5) * 0.1)); }
      c.add(new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts), 80, 0.022 + rand() * 0.02, 6, false), fibMat));
    }
    c.position.set(x, y, (rand() - 0.5) * 2); c.rotation.z = rand() * TAU; group.add(c); cells.push({ c, ph: rand() * TAU });
  }
  const bgFib = new THREE.MeshStandardMaterial({ color: 0xf08a98, emissive: 0xd6141f, emissiveIntensity: 0.15, roughness: 0.6, transparent: true, opacity: 0.12 });
  for (let f = 0; f < 16; f++) {
    const pts = []; const y0 = (rand() - 0.5) * 14, a = (rand() - 0.5) * 0.5;
    for (let k = 0; k <= 10; k++) { const x = -16 + k * 3.2; pts.push(new THREE.Vector3(x, y0 + Math.tan(a) * x + Math.sin(k * 0.9 + f) * 0.5, -1 + (rand() - 0.5) * 0.8)); }
    group.add(new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts), 200, 0.014 + rand() * 0.01, 6, false), bgFib));
  }
  function renderAt(t) {
    const p = (t / D) * TAU; const k = 0.5 - 0.5 * Math.cos(p);
    fibMat.opacity = 0.1 + 0.7 * k; fibMat.emissiveIntensity = 0.2 + 0.7 * k; bgFib.opacity = 0.06 + 0.3 * k;
    for (const it of cells) { it.c.rotation.z += 0; it.c.position.z = Math.sin(p + it.ph) * 0.3; }
    group.rotation.z = Math.sin(p) * 0.04;
    camera.position.set(Math.sin(p) * 0.8, Math.cos(p) * 0.5, 22 - k * 3); camera.lookAt(0, 0, 0);
    renderer.render(scene, camera);
  }
""")

for name, (title, body) in SCENES.items():
    d = os.path.join(ROOT, name); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(HTML.format(W=W, H=H, D=D, title=title, scene=body))
print("ok", list(SCENES))
