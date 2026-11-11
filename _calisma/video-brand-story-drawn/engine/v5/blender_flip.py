# Blender page turn, page layer only: the finished sketch page turns over the left spine (real bent geometry).
# The sheet keeps its photo tone exactly (emission), curvature shading comes from the surface normal against the
# window light; the back shows plain paper with the ink faintly through. Rendered on a transparent film so the
# page below and the contact shadow are composited in python on the same pixels as the rest of the film.
# usage: blender -b -P blender_flip.py -- FRONT.png OUTDIR [frames]
import bpy, bmesh, math, sys, os
from mathutils import Vector

argv = sys.argv[sys.argv.index('--') + 1:]
FRONT, OUTDIR = argv[0], argv[1]
NF = int(argv[2]) if len(argv) > 2 else 54
os.makedirs(OUTDIR, exist_ok=True)

W, H = 1080, 1920
PH = 1.6; PW = PH * W / H
NU, NV = 100, 140

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
eng = [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties['engine'].enum_items]
sc.render.engine = 'BLENDER_EEVEE_NEXT' if 'BLENDER_EEVEE_NEXT' in eng else 'BLENDER_EEVEE'
sc.render.resolution_x, sc.render.resolution_y = W, H
sc.render.film_transparent = True
sc.view_settings.view_transform = 'Standard'
sc.render.image_settings.color_mode = 'RGBA'

m = bpy.data.materials.new('page'); m.use_nodes = True; nt = m.node_tree; nt.nodes.clear(); L = nt.links
out = nt.nodes.new('ShaderNodeOutputMaterial')
tex = nt.nodes.new('ShaderNodeTexImage'); tex.image = bpy.data.images.load(FRONT); tex.interpolation = 'Cubic'
geo = nt.nodes.new('ShaderNodeNewGeometry')
# normal facing the viewer side of the sheet
neg = nt.nodes.new('ShaderNodeVectorMath'); neg.operation = 'SCALE'; neg.inputs['Scale'].default_value = -1
L.new(geo.outputs['Normal'], neg.inputs[0])
nsel = nt.nodes.new('ShaderNodeMix'); nsel.data_type = 'VECTOR'
L.new(geo.outputs['Backfacing'], nsel.inputs['Factor']); L.new(geo.outputs['Normal'], nsel.inputs[4]); L.new(neg.outputs[0], nsel.inputs[5])
# window light from the upper left, a little toward the camera
dot = nt.nodes.new('ShaderNodeVectorMath'); dot.operation = 'DOT_PRODUCT'
lv = Vector((-0.35, 0.45, 0.82)).normalized(); dot.inputs[1].default_value = lv
L.new(nsel.outputs[1], dot.inputs[0])
# shade = (0.45 + 0.55*max(0,dot)) / (0.45 + 0.55*lz)  -> exactly 1.0 when the sheet lies flat
mx = nt.nodes.new('ShaderNodeMath'); mx.operation = 'MAXIMUM'; mx.inputs[1].default_value = 0.0; L.new(dot.outputs['Value'], mx.inputs[0])
ma = nt.nodes.new('ShaderNodeMath'); ma.operation = 'MULTIPLY_ADD'; ma.inputs[1].default_value = 0.55; ma.inputs[2].default_value = 0.45; L.new(mx.outputs[0], ma.inputs[0])
nm = nt.nodes.new('ShaderNodeMath'); nm.operation = 'DIVIDE'; nm.inputs[1].default_value = 0.45 + 0.55 * lv.z; L.new(ma.outputs[0], nm.inputs[0])
# back of the sheet: paper with the ink faintly showing through (UVs mirror it automatically)
back = nt.nodes.new('ShaderNodeMix'); back.data_type = 'RGBA'; back.inputs['Factor'].default_value = 0.07
back.inputs[6].default_value = (0.86, 0.83, 0.79, 1); L.new(tex.outputs['Color'], back.inputs[7])
side = nt.nodes.new('ShaderNodeMix'); side.data_type = 'RGBA'
L.new(geo.outputs['Backfacing'], side.inputs['Factor']); L.new(tex.outputs['Color'], side.inputs[6]); L.new(back.outputs[2], side.inputs[7])
shade = nt.nodes.new('ShaderNodeMix'); shade.data_type = 'RGBA'; shade.blend_type = 'MULTIPLY'; shade.inputs['Factor'].default_value = 1.0
L.new(side.outputs[2], shade.inputs[6])
cmb = nt.nodes.new('ShaderNodeCombineColor'); [L.new(nm.outputs[0], cmb.inputs[i]) for i in range(3)]
L.new(cmb.outputs[0], shade.inputs[7])
em = nt.nodes.new('ShaderNodeEmission'); em.inputs['Strength'].default_value = 1.0
L.new(shade.outputs[2], em.inputs['Color']); L.new(em.outputs[0], out.inputs[0])
m.use_backface_culling = False

me = bpy.data.meshes.new('page'); bm = bmesh.new()
verts = [[bm.verts.new((-PW / 2 + PW * i / NU, -PH / 2 + PH * j / NV, 0)) for j in range(NV + 1)] for i in range(NU + 1)]
uv = bm.loops.layers.uv.new()
for i in range(NU):
    for j in range(NV):
        f = bm.faces.new((verts[i][j], verts[i + 1][j], verts[i + 1][j + 1], verts[i][j + 1]))
        for lp, (a, b) in zip(f.loops, ((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1))):
            lp[uv].uv = (a / NU, b / NV)
bm.to_mesh(me); bm.free()
page = bpy.data.objects.new('page', me); sc.collection.objects.link(page); me.materials.append(m)
for p in me.polygons: p.use_smooth = True

# camera straight down, the flat sheet fills the frame exactly (perspective, so the lifted part comes closer)
cam = bpy.data.cameras.new('cam'); cam.lens = 50; cam.sensor_fit = 'VERTICAL'; cam.sensor_height = 36
co = bpy.data.objects.new('cam', cam); sc.collection.objects.link(co); sc.camera = co
dist = (PH / 2) / math.tan(math.atan(18 / 50))
co.location = (0, 0, dist); co.rotation_euler = (0, 0, 0)

base = [v.co.copy() for v in me.vertices]


def ease(t): return t * t * (3 - 2 * t)


def pose(t):
    """the free side lifts first (bottom corner leading), the sheet rolls over the spine at the left edge"""
    phi = math.pi * ease(t)
    bend = 1.4 * math.sin(math.pi * t)
    for v, b in zip(me.vertices, base):
        s = b.x + PW / 2
        yn = (b.y + PH / 2) / PH
        k = bend * (1.3 - 0.6 * yn)
        n = 28; x = 0.0; z = 0.0; ds = s / n
        for i in range(n):
            u = (i + 0.5) * ds / PW
            w0 = 0.35 + 0.65 * ease(t)                               # the spine side catches up so the sheet lands flat on the left
            a = min(math.pi, phi * (w0 + (1 - w0) * min(1, u * 1.6)) + k * u ** 1.5)
            x += math.cos(a) * ds; z += math.sin(a) * ds
        v.co = Vector((-PW / 2 + x, b.y, z))
    me.update()


for f in range(NF):
    t = f / (NF - 1)
    pose(t)
    sc.render.filepath = os.path.join(OUTDIR, f'f{f:03d}.png')
    bpy.ops.render.render(write_still=True)
print('DONE', OUTDIR)
