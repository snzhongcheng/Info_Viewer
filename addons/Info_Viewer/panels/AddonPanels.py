import bpy

from ..config import __addon_name__
from ....common.i18n.i18n import i18n
from ....common.types.framework import reg_order

@reg_order(0)# ==========显示面板==========
class VIEW3D_PT_InfoViewerViewer(bpy.types.Panel):
    bl_label = "Viewer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Info Viewer"

    def draw(self, context: bpy.types.Context):

        layout = self.layout
        row_Viewer = layout.row()

        split = row_Viewer.split(factor=0.3)

        col_Name = split.column()
        col_Name.label(text="bl_idname")
        col_Name.label(text="bl_label")
        col_Name.label(text="name ")
        col_Name.label(text="name_full")
        col_Name.label(text="type")
        

        col_Value = split.column()
        col_Value.operator("infoviewer.copy_bl_idname",text=" " + context.scene.view_bl_idname + " ")
        col_Value.operator("infoviewer.copy_bl_label",text=" " + context.scene.view_bl_label + " ")
        col_Value.operator("infoviewer.copy_view_name",text=" " + context.scene.view_name + " ")
        col_Value.operator("infoviewer.copy_view_name_full",text=" " + context.scene.view_name_full + " ")
        col_Value.operator("infoviewer.copy_view_type",text=" " + context.scene.view_type + " ")
        

@reg_order(1)# ==========操作面板==========
class VIEW3D_PT_InfoViewerOperators(bpy.types.Panel):
    bl_label = "Operators"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Info Viewer"

    def draw(self, context: bpy.types.Context):
        
        layout = self.layout

        row_Operators = layout.row()
        row_Operators.operator("infoviewer.git_object_info", icon="OBJECT_DATA")
        row_Operators.operator("infoviewer.git_node_info", icon="NODETREE")
