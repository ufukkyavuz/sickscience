# 2.5D lab-notebook still: real 3D desk, notebook, prints, glassware; flat hand-drawn pages
import bpy, bmesh, json, math, os, sys
from mathutils import Vector
R = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[sys.argv.index('--') + 1] if '--' in sys.argv else os.path.join(R, 'still.png')
SAMPLES = int(os.environ.get('SAMPLES', 160))
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'; sc.cycles.samples = SAMPLES; sc.cycles.use_denoising = True
sc.cycles.max_bounces = 24; sc.cycles.transmission_bounces = 24; sc.cycles.glossy_bounces = 12; sc.cycles.transparent_max_bounces = 24
prefs = bpy.context.preferences.addons['cycles'].preferences
prefs.compute_device_type = 'METAL'; prefs.get_devices()
for dv in prefs.devices: dv.use = True
sc.cycles.device = 'GPU'
sc.render.resolution_x, sc.render.resolution_y = 1080, 1920
sc.view_settings.view_transform = 'AgX'; sc.view_settings.look = 'AgX - Medium High Contrast'
sc.view_settings.exposure = -0.2

S = 0.42 / 2040            # metres per spread pixel
PW, PH = 1020 * S, 1480 * S

def mat(name, col, rough=0.5, spec=0.5, tex=None, transm=0.0, ior=1.45, alpha=1.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*col, 1); b.inputs['Roughness'].default_value = rough
    b.inputs['Transmission Weight'].default_value = transm; b.inputs['IOR'].default_value = ior
    b.inputs['Alpha'].default_value = alpha
    if tex:
        t = m.node_tree.nodes.new('ShaderNodeTexImage'); t.image = bpy.data.images.load(tex)
        t.interpolation = 'Cubic'
        m.node_tree.links.new(t.outputs['Color'], b.inputs['Base Color'])
    return m

def grid_obj(name, w, h, nx, ny, zf):
    me = bpy.data.meshes.new(name); bm = bmesh.new()
    verts = [[bm.verts.new((-w / 2 + w * i / nx, -h / 2 + h * j / ny, 0)) for j in range(ny + 1)] for i in range(nx + 1)]
    uv = bm.loops.layers.uv.new()
    for i in range(nx):
        for j in range(ny):
            f = bm.faces.new((verts[i][j], verts[i + 1][j], verts[i + 1][j + 1], verts[i][j + 1]))
            for l in f.loops:
                co = l.vert.co; l[uv].uv = ((co.x + w / 2) / w, (co.y + h / 2) / h)
    for v in bm.verts: v.co.z = zf(v.co.x, v.co.y)
    bm.to_mesh(me); o = bpy.data.objects.new(name, me); sc.collection.objects.link(o)
    for p in me.polygons: p.use_smooth = True
    return o

# ---- world + light
w = bpy.data.worlds.new('W'); sc.world = w; w.use_nodes = True
env = w.node_tree.nodes.new('ShaderNodeTexEnvironment'); env.image = bpy.data.images.load(os.path.join(R, 'hdri', 'studio.hdr'))
bg = w.node_tree.nodes['Background']; bg.inputs['Strength'].default_value = 0.4
w.node_tree.links.new(env.outputs['Color'], bg.inputs['Color'])
mix = w.node_tree.nodes.new('ShaderNodeMixRGB'); mix.inputs['Fac'].default_value = 1.0; mix.inputs['Color2'].default_value = (0.95, 0.95, 0.95, 1)
w.node_tree.links.new(env.outputs['Color'], mix.inputs['Color1']); w.node_tree.links.new(mix.outputs['Color'], bg.inputs['Color'])
sun = bpy.data.lights.new('sun', 'SUN'); sun.energy = 4.5; sun.angle = math.radians(2.5); sun.color = (1.0, 0.96, 0.9)
so = bpy.data.objects.new('sun', sun); sc.collection.objects.link(so); so.rotation_euler = (math.radians(38), math.radians(-22), math.radians(-35))
ar = bpy.data.lights.new('soft', 'AREA'); ar.energy = 30; ar.size = 1.2
ao = bpy.data.objects.new('soft', ar); sc.collection.objects.link(ao); ao.location = (-0.6, 0.5, 0.9); ao.rotation_euler = (math.radians(-20), math.radians(-25), 0)

# ---- desk
desk = grid_obj('desk', 3, 3, 1, 1, lambda x, y: 0)
dm = mat('desk', (0.93, 0.93, 0.92), rough=0.42)
nt = dm.node_tree; nz = nt.nodes.new('ShaderNodeTexNoise'); nz.inputs['Scale'].default_value = 900; nz.inputs['Detail'].default_value = 6
bp = nt.nodes.new('ShaderNodeBump'); bp.inputs['Strength'].default_value = 0.04
nt.links.new(nz.outputs['Fac'], bp.inputs['Height']); nt.links.new(bp.outputs['Normal'], nt.nodes['Principled BSDF'].inputs['Normal'])
desk.data.materials.append(dm)

# ---- notebook: hard cover, page blocks, curved top pages
TH = 0.009                                         # page block thickness
cover = grid_obj('cover', 2 * PW + 0.016, PH + 0.016, 1, 1, lambda x, y: 0.0012)
bpy.context.view_layer.objects.active = cover
cm = mat('cover', (0.86, 0.86, 0.85), rough=0.75); cover.data.materials.append(cm)
sol = cover.modifiers.new('s', 'SOLIDIFY'); sol.thickness = 0.0024
def curve(xc):  # page lift: rises from the spine, flat across, slight drop at the outer edge
    d = abs(xc)
    return TH * (1 - math.exp(-d / 0.018)) - 0.0018 * max(0, (d - PW + 0.02) / 0.02) ** 2
for side, tex in ((-1, 'tex_left.png'), (1, 'tex_right.png')):
    blk = grid_obj(f'block{side}', PW - 0.002, PH - 0.004, 120, 1, lambda x, y, s=side: 0)
    blk.location.x = side * PW / 2
    for v in blk.data.vertices: v.co.z = 0.0026 + curve(v.co.x + side * PW / 2) - 0.0006
    bs = blk.modifiers.new('s', 'SOLIDIFY'); bs.thickness = 0.007; bs.offset = -1
    blk.data.materials.append(mat('edge', (0.95, 0.94, 0.9), rough=0.9))
    pg = grid_obj(f'page{side}', PW, PH, 160, 2, lambda x, y: 0)
    pg.location.x = side * PW / 2
    for v in pg.data.vertices: v.co.z = 0.0026 + curve(v.co.x + side * PW / 2) + 0.0002
    pg.data.materials.append(mat(f'page{side}', (1, 1, 1), rough=0.82, tex=os.path.join(R, tex)))

def page_z(px):
    x = (px - 1020) * S
    return 0.0028 + curve(x) + 0.0003

# ---- prints with tape
for i, p in enumerate(json.load(open(os.path.join(R, 'prints.json')))):
    cx, cy = p['c']; w = p['w'] * S; h = w * p['aspect']
    o = grid_obj(f'print{p["y"]}', w, h, 6, 6, lambda x, y: 0.0004 * (x / w) ** 2 * 4)   # tiny curl
    o.location = ((cx - 1020) * S, (740 - cy) * S, page_z(cx) + 0.0004 * i)
    o.rotation_euler.z = math.radians(-p['r'])
    s2 = o.modifiers.new('s', 'SOLIDIFY'); s2.thickness = 0.0003
    o.data.materials.append(mat(f'ph{p["y"]}', (1, 1, 1), rough=0.32, tex=os.path.join(R, f'print_{p["y"]}.jpg')))
    tm = mat(f'tape{i}', (0.97, 0.95, 0.88), rough=0.5, alpha=0.6)
    for k, sx in enumerate((-1, 1)):
        tp = grid_obj(f'tape{i}{k}', 0.022, 0.009, 2, 1, lambda x, y: 0)
        tp.parent = o; tp.location = (sx * (w / 2 - 0.004), h / 2 - 0.004, 0.0006); tp.rotation_euler.z = math.radians(-40 * sx)
        tp.data.materials.append(tm)

for y, (px, py, rz, pw) in {2018: (-0.165, 0.222, 9, 0.09), 2025: (0.15, 0.232, -7, 0.10), 2024: (0.17, -0.235, 6, 0.085)}.items():
    o = grid_obj(f'desk{y}', pw, pw * 1.18, 4, 4, lambda x, y_: 0.0002)
    o.location = (px, py, 0.0); o.rotation_euler.z = math.radians(rz)
    o.modifiers.new('s', 'SOLIDIFY').thickness = 0.0003
    o.data.materials.append(mat(f'dk{y}', (1, 1, 1), rough=0.3, tex=os.path.join(R, f'print_{y}.jpg')))

# ---- props (hero-free, quiet lab still life)
glass = mat('glass', (1, 1, 1), rough=0.03, transm=1.0, ior=1.45)
def shadow_clear(m, k=0.85):   # glass lets light through for shadow rays (no caustics in Cycles otherwise -> black glass)
    nt_ = m.node_tree; out = nt_.nodes['Material Output']; bsdf = nt_.nodes['Principled BSDF']
    lp = nt_.nodes.new('ShaderNodeLightPath'); tr = nt_.nodes.new('ShaderNodeBsdfTransparent'); mx = nt_.nodes.new('ShaderNodeMixShader')
    mt = nt_.nodes.new('ShaderNodeMath'); mt.operation = 'MULTIPLY'; mt.inputs[1].default_value = k
    nt_.links.new(lp.outputs['Is Shadow Ray'], mt.inputs[0]); nt_.links.new(mt.outputs[0], mx.inputs['Fac'])
    nt_.links.new(bsdf.outputs[0], mx.inputs[1]); nt_.links.new(tr.outputs[0], mx.inputs[2]); nt_.links.new(mx.outputs[0], out.inputs['Surface'])
shadow_clear(glass)
milk = mat('milk', (0.96, 0.95, 0.9), rough=0.25, transm=0.55, ior=1.35); shadow_clear(milk, 0.4)
def cyl(name, r, h, loc, m, verts=64):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=h, location=(loc[0], loc[1], loc[2] + h / 2))
    o = bpy.context.object; o.name = name; o.data.materials.append(m); bpy.ops.object.shade_smooth(); return o
# beaker (open glass shell) with milky liquid
bk = cyl('beaker', 0.034, 0.085, (-0.02, 0.33, 0), glass); bpy.ops.object.modifier_add(type='SOLIDIFY'); bk.modifiers[-1].thickness = 0.0025
bm_ = bmesh.new(); bm_.from_mesh(bk.data); top = [f for f in bm_.faces if f.normal.z > 0.9]; bmesh.ops.delete(bm_, geom=top, context='FACES'); bm_.to_mesh(bk.data)
cyl('liquid', 0.0315, 0.05, (-0.02, 0.33, 0.003), milk)
# flask
# petri dish with pineapple slice
pd = cyl('petri', 0.05, 0.013, (-0.16, -0.30, 0), glass)
bm_ = bmesh.new(); bm_.from_mesh(pd.data); bmesh.ops.delete(bm_, geom=[f for f in bm_.faces if f.normal.z > 0.9], context='FACES'); bm_.to_mesh(pd.data)
pd.modifiers.new('s', 'SOLIDIFY').thickness = 0.0015
pin = mat('pine', (1, 1, 1), rough=0.35, tex=os.path.join(R, 'pineapple.png'))
pb = pin.node_tree.nodes['Principled BSDF']; ti = [n for n in pin.node_tree.nodes if n.type == 'TEX_IMAGE'][0]
pin.node_tree.links.new(ti.outputs['Alpha'], pb.inputs['Alpha']); pb.inputs['Subsurface Weight'].default_value = 0.25
pp = grid_obj('pineapple', 0.077, 0.077, 1, 1, lambda x, y: 0); pp.location = (-0.16, -0.30, 0.0035); pp.rotation_euler.z = math.radians(15)
pp.modifiers.new('s', 'SOLIDIFY').thickness = 0.003; pp.data.materials.append(pin)
# pipette and pen
pip = cyl('pipette', 0.004, 0.16, (0, 0, 0), glass, 24); pip.location = (-0.09, -0.24, 0.004); pip.rotation_euler = (0, math.radians(90), math.radians(-60))
penm = mat('pen', (0.02, 0.02, 0.022), rough=0.3)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.009, location=(-0.09 - 0.08 * math.cos(math.radians(-60)) * 1.0, -0.24 - 0.08 * math.sin(math.radians(-60)), 0.009))
bb = bpy.context.object; bb.scale = (1.6, 1, 1); bb.rotation_euler.z = math.radians(-60); bb.data.materials.append(milk); bpy.ops.object.shade_smooth()
pen = cyl('pen', 0.0055, 0.14, (0, 0, 0), penm, 32); pen.location = (0.03, -0.31, 0.0055); pen.rotation_euler = (0, math.radians(90), math.radians(-28))
sl = grid_obj('slide', 0.026, 0.075, 1, 1, lambda x, y: 0.0012); sl.location = (-0.03, -0.36, 0); sl.rotation_euler.z = math.radians(20)
sl.data.materials.append(glass); sl.modifiers.new('s', 'SOLIDIFY').thickness = 0.0012

# ---- camera: slightly tilted top-down, like the film's look
cam = bpy.data.cameras.new('cam'); cam.lens = 50; cam.sensor_fit = 'HORIZONTAL'; cam.sensor_width = 36
cam.dof.use_dof = True; cam.dof.focus_distance = 0.69; cam.dof.aperture_fstop = 4.0
co = bpy.data.objects.new('cam', cam); sc.collection.objects.link(co); sc.camera = co
tilt = math.radians(float(os.environ.get('TILT', 9)))
dist = 0.69
co.location = (0, -math.sin(tilt) * dist, math.cos(tilt) * dist + 0.003)
co.rotation_euler = (tilt, 0, 0)
sc.render.filepath = OUT
bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(R, 'notebook_still.blend'))
print('RENDERED', OUT)
