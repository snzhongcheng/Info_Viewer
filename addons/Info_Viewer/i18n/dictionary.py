from common.i18n.dictionary import preprocess_dictionary

dictionary = {
    "zh_CN": {
        "Get Object's Info":"获得物体信息",
        "Get object's info":"获得物体信息",
        "Get Node's Info":"获得节点信息",
        "Get node's info":"获得节点信息",
        "Copy bl_idname":"复制 bl_idname",
        "Copy bl_label":"复制 bl_label",
        "Copy name":"复制name",
        "Copy name_full":"复制name_full",
        "Copy type":"复制type",
    }
}

dictionary = preprocess_dictionary(dictionary)

dictionary["zh_HANS"] = dictionary["zh_CN"]
