"""
This is NOT for running standalone. You must use it as a blender script
"""
import sys
import bpy
# required for import
token = '/' if '/' == bpy.data.filepath[0] else '\\'  # cross-OS
sys.path.append(
    token.join(bpy.data.filepath.split(token)[:-2])
)
from electromagnetism import ChargeSystem, Charge, process_coordinates, FixedCharge


def electron_animation_from_coords(name: str, coords: list, initial_location=(0, 0, 0), frames_per_keyframe=1) -> None:
    """
    Animate an electron from a list of coordinates
    :param name: name of the mesh
    :param coords: animation coords
    :param initial_location: location upon mesh creation
    :param frames_per_keyframe: # of frames after each keyframe
    """
    electron_mesh = bpy.ops.mesh.primitive_uv_sphere_add(location=initial_location)
    electron_object = bpy.context.object
    electron_object.name = name

    for f, coord in enumerate(coords):
        electron_object.location = tuple(coord)
        electron_object.keyframe_insert("location", frame=f * frames_per_keyframe)

v = ChargeSystem(3)
c1 = FixedCharge(1e-5, v, position=[-10, 0, 0])
c2 = Charge(-2.5e-5, v, position=[2.1, -10, -10])
c3 = FixedCharge(1 * 10 ** -5, v, position=[10, 0, 0])
anim = process_coordinates(v, 1200)
for ind, charge_coords in enumerate(anim):
    electron_animation_from_coords('electron{}'.format(ind), charge_coords, initial_location=charge_coords[0])
