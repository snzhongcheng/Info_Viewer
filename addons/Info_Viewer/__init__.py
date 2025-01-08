import bpy

from .config import __addon_name__
from .i18n.dictionary import dictionary
from ...common.class_loader import auto_load
from ...common.class_loader.auto_load import add_properties, remove_properties
from ...common.i18n.dictionary import common_dictionary
from ...common.i18n.i18n import load_dictionary
from bpy.props import StringProperty, IntProperty, BoolProperty, EnumProperty

# Add-on info
bl_info = {
    "name": "Info Viewer/信息查看器",
    "author": "少年忠城-snzhongcheng",
    "blender": (4, 2, 0),
    "version": (1, 0, 0),
    "description": "Easier to see the info of the active object and node",
    "warning": "",
    "doc_url": "https://github.com/snzhongcheng/Info_Viewer",
    "tracker_url": "https://space.bilibili.com/455309610",
    "support": "COMMUNITY",
    "category": "Development"
}

_addon_properties = {
    bpy.types.Scene: {
        "view_bl_idname": StringProperty(name="view_bl_idname", default=""),
        "view_bl_label": StringProperty(name="view_bl_label", default=""),
        "view_name": StringProperty(name="view_name", default=""),
        "view_name_full": StringProperty(name="view_name_full", default=""),
        "view_type": StringProperty(name="view_type", default=""),
        }
}


# You may declare properties like following, framework will automatically add and remove them.
# Do not define your own property group class in the __init__.py file. Define it in a separate file and import it here.
# 注意不要在__init__.py文件中自定义PropertyGroup类。请在单独的文件中定义它们并在此处导入。
# _addon_properties = {
#     bpy.types.Scene: {
#         "property_name": bpy.props.StringProperty(name="property_name"),
#     },
# }

def register():
    # Register classes
    auto_load.init()
    auto_load.register()
    add_properties(_addon_properties)

    # Internationalization
    load_dictionary(dictionary)
    bpy.app.translations.register(__addon_name__, common_dictionary)

    print("{} addon is installed.".format(__addon_name__))


def unregister():
    # Internationalization
    bpy.app.translations.unregister(__addon_name__)
    # unRegister classes
    auto_load.unregister()
    remove_properties(_addon_properties)
    print("{} addon is uninstalled.".format(__addon_name__))
