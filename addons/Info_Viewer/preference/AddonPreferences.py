import os

import bpy
from bpy.props import StringProperty, IntProperty, BoolProperty
from bpy.types import AddonPreferences

from ..config import __addon_name__


class InfoViewerAddonPreferences(AddonPreferences):
    bl_idname = __addon_name__

    # def draw(self, context: bpy.types.Context):
    #     layout = self.layout
