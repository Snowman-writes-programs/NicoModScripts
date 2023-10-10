import bpy
from mathutils import Vector

# 获取当前选中的物体
selected_object = bpy.context.object

# 创建骨骼
bpy.ops.object.armature_add()
armature_object = bpy.context.object
armature = armature_object.data

# 切换到编辑模式
bpy.ops.object.mode_set(mode='EDIT')

# 遍历所有的顶点组
for vertex_group in selected_object.vertex_groups:
    # 获取顶点组的名称
    vertex_group_name = vertex_group.name

    # 创建骨骼
    bone = armature.edit_bones.new(vertex_group_name)

    # 根据顶点组位置生成骨骼
    for vertex in selected_object.data.vertices:
        for group_element in vertex.groups:
            if group_element.group == vertex_group.index:
                # 获取顶点位置
                vertex_position = selected_object.matrix_world @ vertex.co

                # 设置骨骼位置
                bone.head = vertex_position
                bone.tail = Vector(vertex_position) + Vector((0, 0, 0.1))  # 设置骨骼长度

                # 分配顶点到骨骼
                bone_vertex_group = selected_object.vertex_groups[vertex_group_name]
                bone_vertex_group.add([vertex.index], 0, 'ADD')

# 刷新场景
bpy.context.view_layer.update()

# 切换回对象模式
bpy.ops.object.mode_set(mode='OBJECT')


'''
bpy.ops.object: 包含操作物体的函数，如armature_add()和mode_set()。
bpy.context: 提供对当前上下文的访问，可以获取选中的物体。
bpy.types.Armature: 骨骼对象的类型，包含edit_bones属性。
bpy.types.EditBone: 编辑模式下的骨骼对象类型，包含head和tail属性。
bpy.types.VertexGroup: 顶点组对象类型，包含name属性。
'''