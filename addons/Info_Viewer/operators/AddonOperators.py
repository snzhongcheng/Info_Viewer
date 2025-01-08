import bpy

from ..config import __addon_name__

class INFOVIEWER_OT_GetObjectInfo(bpy.types.Operator):# 获取物体信息
    bl_label = "Get Object's Info"
    bl_idname = "infoviewer.get_object_info"
    bl_description = "Get object's info"
    bl_options = {'REGISTER','UNDO'}
    
    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.selected_objects
    
    def execute(self, context: bpy.types.Context):
        context.scene.view_bl_idname = "None"
        context.scene.view_bl_label = "None"
        context.scene.view_name = context.active_object.name
        context.scene.view_name_full = context.active_object.name_full
        context.scene.view_type = context.active_object.type
        
        return {'FINISHED'}

class INFOVIEWER_OT_GetMaterialNodeInfo(bpy.types.Operator):# 获取材质节点信息
    bl_label = "Get Material Node's Info"
    bl_idname = "infoviewer.get_material_node_info"
    bl_description = "Get material node's info"
    bl_options = {'REGISTER','UNDO'}
    
    @classmethod
    def poll(cls, context: bpy.types.Context):
        if context.active_object.active_material:
            if context.active_object.active_material.node_tree.nodes.active != None:
                return True
    
    def execute(self, context: bpy.types.Context):
        node = context.active_object.active_material.node_tree.nodes.active
        context.scene.view_bl_idname = node.bl_idname
        context.scene.view_bl_label = node.bl_label
        context.scene.view_name = node.name
        context.scene.view_name_full = "None"
        context.scene.view_type = node.type
        return {'FINISHED'}

class INFOVIEWER_OT_GetGeometryNodeInfo(bpy.types.Operator):# 获取几何节点信息
    bl_label = "Get Geometry Node's Info"
    bl_idname = "infoviewer.get_geometry_node_info"
    bl_description = "Get geometry node's info"
    bl_options = {'REGISTER','UNDO'}
    
    @classmethod
    def poll(cls, context: bpy.types.Context):
        if "node_group" in dir(context.active_object.modifiers.active):
            if "nodes" in dir(context.active_object.modifiers.active.node_group):
                if context.active_object.modifiers.active.node_group.nodes.active != None:
                    return True

    def execute(self, context: bpy.types.Context):
        node = context.active_object.modifiers.active.node_group.nodes.active
        context.scene.view_bl_idname = node.bl_idname
        context.scene.view_bl_label = node.bl_label
        context.scene.view_name = node.name
        context.scene.view_name_full = "None"
        context.scene.view_type = node.type
        return {'FINISHED'}

class INFOVIEWER_OT_Copy_bl_idname(bpy.types.Operator):# 复制bl_idname
    bl_label = "Copy bl_idname"
    bl_idname = "infoviewer.copy_bl_idname"
    bl_description = "Copy bl_idname"

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.scene.view_bl_idname != "None"

    def execute(self, context: bpy.types.Context):
        context.window_manager.clipboard = context.scene.view_bl_idname
        return {'FINISHED'}

class INFOVIEWER_OT_Copy_bl_label(bpy.types.Operator):# 复制bl_label
    bl_label = "Copy bl_label"
    bl_idname = "infoviewer.copy_bl_label"
    bl_description = "Copy bl_label"

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.scene.view_bl_label != "None"

    def execute(self, context):
        context.window_manager.clipboard = context.scene.view_bl_label
        return {'FINISHED'}

class INFOVIEWER_OT_Copy_view_name(bpy.types.Operator):# 复制name
    bl_label = "Copy name"
    bl_idname = "infoviewer.copy_view_name"
    bl_description = "Copy name"

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.scene.view_name != "None"

    def execute(self, context):
        bpy.context.window_manager.clipboard = context.scene.view_name
        return {'FINISHED'}

class INFOVIEWER_OT_Copy_view_name_full(bpy.types.Operator):# 复制name_full
    bl_label = "Copy name_full"
    bl_idname = "infoviewer.copy_view_name_full"
    bl_description = "Copy name_full"

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.scene.view_name_full != "None"

    def execute(self, context):
        bpy.context.window_manager.clipboard = context.scene.view_name_full
        return {'FINISHED'}

class INFOVIEWER_OT_Copy_view_type(bpy.types.Operator):# 复制type
    bl_label = "Copy type"
    bl_idname = "infoviewer.copy_view_type"
    bl_description = "Copy type"

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.scene.view_type != "None"

    def execute(self, context):
        bpy.context.window_manager.clipboard = context.scene.view_type
        return {'FINISHED'}
