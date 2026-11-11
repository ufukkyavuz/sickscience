# prints as real 3D objects over the exact previous scene (photo plate + ink); shadow catcher, light matched to the photo
import bpy, bmesh, json, math, os, sys
from mathutils import Vector
R = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[sys.argv.index('--') + 1]
SAMPLES = int(os.environ.get('SAMPLES', 128))
P = json.load(open(os.path.join(R, 'plate_ink.json'))); PWp, PHp = P['size']; DX, DY = P['OX'] - P['box'][0], P['OY'] - P['box'][1]
S = 0.42 / 2040
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.render.engine = 'CYCLES'; sc.cycles.samples = SAMPLES; sc.cycles.use_denoising = True
prefs = bpy.context.preferences.addons['cycles'].preferences; prefs.compute_device_type = 'METAL'; prefs.get_devices()
for dv in prefs.devices: dv.use = True
sc.cycles.device = 'GPU'; sc.render.film_transparent = True
sc.render.resolution_x, sc.render.resolution_y = PWp, PHp
sc.view_settings.view_transform = 'Standard'; sc.view_settings.exposure = float(os.environ.get('EXPO', 0))

def to3d(px, py): return ((px - PWp / 2) * S, (PHp / 2 - py) * S)
def grid_obj(name, w, h, nx, ny, zf):
    me = bpy.data.meshes.new(name); bm = bmesh.new()
    V = [[bm.verts.new((-w / 2 + w * i / nx, -h / 2 + h * j / ny, 0)) for j in range(ny + 1)] for i in range(nx + 1)]
    uv = bm.loops.layers.uv.new()
    for i in range(nx):
        for j in range(ny):
            f = bm.faces.new((V[i][j], V[i + 1][j], V[i + 1][j + 1], V[i][j + 1]))
            for l in f.loops: l[uv].uv = ((l.vert.co.x + w / 2) / w, (l.vert.co.y + h / 2) / h)
    for v in bm.verts: v.co.z = zf(v.co.x, v.co.y)
    bm.to_mesh(me); o = bpy.data.objects.new(name, me); sc.collection.objects.link(o)
    for p in me.polygons: p.use_smooth = True
    return o
def mat(name, col, rough=0.5, tex=None, alpha=1.0):
    m = bpy.data.materials.new(name); m.use_nodes = True; b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*col, 1); b.inputs['Roughness'].default_value = rough; b.inputs['Alpha'].default_value = alpha
    if tex:
        t = m.node_tree.nodes.new('ShaderNodeTexImage'); t.image = bpy.data.images.load(tex); t.interpolation = 'Cubic'
        m.node_tree.links.new(t.outputs['Color'], b.inputs['Base Color'])
    return m

# light matched to the photo: soft window light from upper left + white room fill
w = bpy.data.worlds.new('W'); sc.world = w; w.use_nodes = True
w.node_tree.nodes['Background'].inputs['Color'].default_value = (1, 1, 1, 1); w.node_tree.nodes['Background'].inputs['Strength'].default_value = float(os.environ.get('FILL', 0.55))
sun = bpy.data.lights.new('sun', 'SUN'); sun.energy = float(os.environ.get('SUN', 2.2)); sun.angle = math.radians(7); sun.color = (1, 0.985, 0.96)
so = bpy.data.objects.new('sun', sun); sc.collection.objects.link(so)
so.rotation_euler = Vector((0.55, -0.65, -1.0)).normalized().to_track_quat('-Z', 'Y').to_euler()

# shadow catcher = the page/desk surface
cat = grid_obj('catcher', PWp * S * 1.2, PHp * S * 1.2, 1, 1, lambda x, y: 0); cat.is_shadow_catcher = True
cat.data.materials.append(mat('c', (0.95, 0.95, 0.95)))

prints = json.load(open(os.path.join(R, 'prints.json')))
OP = os.environ.get('ONLY_PRINT')
for i, p in enumerate([] if os.environ.get('ONLY_DESK') else prints):
    if OP is not None and i != int(OP): continue
    cx, cy = p['c']; x, y = to3d(cx + DX, cy + DY); w_ = p['w'] * S; h_ = w_ * p['aspect']
    o = grid_obj(f'p{p["y"]}', w_, h_, 8, 8, lambda X, Y: 0.0011 * ((X / w_) ** 2 + (Y / h_) ** 2) * 2)  # slight curl, corners lift
    o.location = (x, y, 0.0003 + 0.0002 * i); o.rotation_euler.z = math.radians(-p['r'])
    o.modifiers.new('s', 'SOLIDIFY').thickness = 0.00035
    o.data.materials.append(mat(f'm{i}', (1, 1, 1), 0.35, os.path.join(R, f'print_{p["y"]}.jpg')))
    tm = mat(f't{i}', (0.93, 0.91, 0.84), 0.45, alpha=0.55)
    for k, sx in enumerate((-1, 1)):
        tp = grid_obj(f'tp{i}{k}', 0.024, 0.009, 4, 1, lambda X, Y: 0.00025 * (1 - (2 * X / 0.024) ** 2))
        tp.parent = o; tp.location = (sx * (w_ / 2 - 0.003), h_ / 2 - 0.003, 0.0012); tp.rotation_euler.z = math.radians(-38 * sx)
        tp.data.materials.append(tm)
for y_, (px, py, rz, wcm) in ({} if os.environ.get('ONLY_PRINT') is not None else json.load(open(os.path.join(R, 'desk.json')))).items():
    x, y = to3d(px, py); w_ = wcm / 100; h_ = w_ * 1.17
    o = grid_obj(f'd{y_}', w_, h_, 8, 8, lambda X, Y: 0.0015 * ((X / w_) ** 2 + (Y / h_) ** 2) * 2)
    o.location = (x, y, 0.0002); o.rotation_euler.z = math.radians(rz)
    o.modifiers.new('s', 'SOLIDIFY').thickness = 0.0004
    o.data.materials.append(mat(f'dm{y_}', (1, 1, 1), 0.3, os.path.join(R, f'print_{y_}.jpg')))

cam = bpy.data.cameras.new('cam'); cam.type = 'ORTHO'; cam.ortho_scale = PHp * S
co = bpy.data.objects.new('cam', cam); sc.collection.objects.link(co); sc.camera = co; co.location = (0, 0, 1.5)
sc.render.filepath = OUT; bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(R, 'notebook_plate.blend'))
print('RENDERED')
