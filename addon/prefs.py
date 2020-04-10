import bpy
from . import utils


class PowerSavePrefs(bpy.types.AddonPreferences):
    bl_idname = utils.addon_name

    base_folder: bpy.props.StringProperty(
        name="Base Folder",
        subtype='FILE_PATH',
    )

    autosave_interval: bpy.props.FloatProperty(
        name="Autosave Interval",
        default=60.0,
    )

    save_on_startup: bpy.props.BoolProperty(
        name="Save on Startup",
        default=True,
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "base_folder")
        layout.prop(self, "autosave_interval")
        layout.prop(self, "save_on_startup")
