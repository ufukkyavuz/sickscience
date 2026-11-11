# Glass-style 3D exosome scene (white scientific look), loopable 5 s @30fps, 1080x1350.
# Exosomes = glass vesicles holding small purple cargo beads, orbiting/approaching a large pale glass cell; the cell's nucleus
# breathes white -> mint (instructions activated), like the reference's grey -> green cells.
import bpy, math, sys, os, random
OUTDIR = sys.argv[sys.argv.index('--') + 1]
N = 120
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'
prefs = bpy.context.preferences.addons['cycles'].preferences
try:
    prefs.compute_device_type = 'METAL'; prefs.get_devices()
    for d in prefs.devices: d.use = True
    sc.cycles.device = 'GPU'
except Exception as e: print('gpu', e)
sc.cycles.samples = 32; sc.cycles.use_denoising = True; sc.cycles.max_bounces = 10; sc.cycles.transmission_bounces = 8; sc.cycles.caustics_reflective = False; sc.cycles.caustics_refractive = False
sc.render.resolution_x, sc.render.resolution_y = 1080, 1350
sc.render.image_settings.file_format = 'PNG'; sc.render.film_transparent = False
sc.frame_start, sc.frame_end = 0, N - 1
sc.view_settings.view_transform = 'Standard'
# world
w = bpy.data.worlds.new('w'); sc.world = w; w.use_nodes = True
bg = w.node_tree.nodes['Background']; bg.inputs[0].default_value = (0.80, 0.86, 0.85, 1); bg.inputs[1].default_value = 1.0
def mat(name, base, rough=0.05, trans=0.0, ior=1.45, emit=None, emit_s=0.0, alpha=1.0):
    m = bpy.data.materials.new(name); m.use_nodes = True; b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = base; b.inputs['Roughness'].default_value = rough
    b.inputs['Transmission Weight'].default_value = trans; b.inputs['IOR'].default_value = ior
    if emit is not None: b.inputs['Emission Color'].default_value = emit; b.inputs['Emission Strength'].default_value = emit_s
    return m
glass = mat('glass', (0.80, 0.93, 0.88, 1), 0.03, 1.0)
shell = mat('shell', (0.86, 0.95, 0.97, 1), 0.04, 1.0)
cargo = mat('cargo', (0.45, 0.0, 0.78, 1), 0.12, 0.0, emit=(0.45, 0.0, 0.78, 1), emit_s=0.35)
cargo2 = mat('cargo2', (0.66, 0.13, 0.75, 1), 0.12, 0.0, emit=(0.66, 0.13, 0.75, 1), emit_s=0.3)
nucleus = mat('nucleus', (0.55, 0.60, 0.58, 1), 0.25, 0.0, emit=(0.55, 0.6, 0.58, 1), emit_s=0.15)
floor = mat('floor', (0.72, 0.80, 0.78, 1), 0.45)
def sphere(name, r, loc, m, seg=64):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=loc, segments=seg, ring_count=seg // 2)
    o = bpy.context.active_object; o.name = name; bpy.ops.object.shade_smooth(); o.data.materials.append(m); return o
# backdrop (cyclorama)
bpy.ops.mesh.primitive_plane_add(size=60, location=(0, 0, -3.2)); bpy.context.active_object.data.materials.append(floor)
bpy.ops.mesh.primitive_plane_add(size=60, location=(0, 8, 0), rotation=(math.pi / 2, 0, 0)); bpy.context.active_object.data.materials.append(floor)
# lights (soft boxes)
for loc, s, rot in (((-5, -6, 6), 9, (0.9, -0.5, -0.6)), ((6, -5, 3), 6, (1.2, 0.5, 0.5))):
    bpy.ops.object.light_add(type='AREA', location=loc); L = bpy.context.active_object; L.data.energy = 1800; L.data.size = s; L.rotation_euler = rot
# camera
bpy.ops.object.camera_add(location=(0, -11, 0.9)); cam = bpy.context.active_object; cam.data.lens = 55; sc.camera = cam
cam.rotation_euler = (math.pi / 2 - 0.04, 0, 0)
# cell
cell = sphere('cell', 1.55, (0.35, 0, -0.55), glass, 96)
nuc = sphere('nuc', 0.5, (0.35, 0.05, -0.55), nucleus, 48)
rim = sphere('rim', 1.58, (0.35, 0, -0.55), shell, 96)
# exosomes
random.seed(7)
exo = []
for k in range(7):
    ph = k / 7 * 2 * math.pi
    s = sphere(f'exo{k}', 0.42 + 0.06 * (k % 3), (0, 0, 0), shell, 48)
    beads = []
    for j in range(4):
        a = j * 1.7 + k; b = sphere(f'b{k}_{j}', 0.095, (0, 0, 0), cargo if j % 2 else cargo2, 24)
        beads.append((b, a))
    exo.append((s, beads, ph, 0.9 + 0.35 * (k % 3), 1 if k % 2 else -1))
for f in range(N):
    t = f / N * 2 * math.pi
    # nucleus colour: white -> mint -> white
    k = 0.5 - 0.5 * math.cos(t)
    nb = nucleus.node_tree.nodes['Principled BSDF']
    col = (0.62 - 0.32 * k, 0.64 + 0.12 * k, 0.62 - 0.30 * k, 1); em = (0.62 - 0.4 * k, 0.66 + 0.2 * k, 0.62 - 0.4 * k, 1)
    nb.inputs['Base Color'].default_value = col; nb.inputs['Emission Color'].default_value = em
    nb.inputs['Base Color'].keyframe_insert('default_value', frame=f); nb.inputs['Emission Color'].keyframe_insert('default_value', frame=f)
    nuc.scale = (1 + 0.06 * k,) * 3; nuc.keyframe_insert('scale', frame=f)
    for s, beads, ph, sp, d in exo:
        ang = d * t * sp + ph
        rad = 2.55 + 0.95 * math.sin(t * 2 + ph) * 0.5 + 0.5 * math.sin(ph * 3)
        x = 0.35 + rad * math.cos(ang) * 1.15; z = -0.55 + rad * math.sin(ang) * 0.9; y = -0.2 + 0.9 * math.sin(ang * 1.0 + ph)
        s.location = (x, y, z); s.keyframe_insert('location', frame=f)
        for b, a in beads:
            r0 = 0.17; b.location = (x + r0 * math.cos(a + t * 3), y + r0 * math.sin(a + t * 3) * 0.6, z + r0 * math.sin(a * 1.3 + t * 2)); b.keyframe_insert('location', frame=f)
    cam.location = (0.25 * math.sin(t), -11 + 0.0, 0.9 + 0.15 * math.cos(t)); cam.keyframe_insert('location', frame=f)
# test one or all frames
frames = [int(x) for x in sys.argv[sys.argv.index('--') + 2:]] if len(sys.argv) > sys.argv.index('--') + 2 else range(N)
for f in frames:
    sc.frame_set(f); sc.render.filepath = os.path.join(OUTDIR, f'f{f:04d}.png'); bpy.ops.render.render(write_still=True)
