import cadquery as cq
import trimesh
import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt # 尽管这里可能不会直接用于渲染，但保留以符合你的demo

import os
import sys

# --- 配置 ---
# 指定你的 CadQuery 模型定义文件路径
# 请确保这个文件存在于与当前脚本相同的目录，或提供完整路径
CADQUERY_SCRIPT_FILE = '/home/user2/wns/cad-recode/cad-recode-v1.5-data-origindpo/dpo_preference_pairs_best_median/train/train_batch_63_630020_gt_code.py'

# 定义输出文件路径
# 注意：你的demo路径是 /home/user2/wns/cad-recode/tmp/1.stl
# 为了在大多数系统上通用且避免权限问题，这里使用当前目录下的 'tmp_output'
OUTPUT_DIR = './tmp'
OUTPUT_STL_FILENAME = 'gt.stl'
OUTPUT_STEP_FILENAME = 'gt.step'
# --- 配置结束 ---

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)
output_stl_path = os.path.join(OUTPUT_DIR, OUTPUT_STL_FILENAME)
output_step_path = os.path.join(OUTPUT_DIR, OUTPUT_STEP_FILENAME)

# --- 严格遵循你提供的逻辑 ---
# 1. 读取 CadQuery 脚本内容
if not os.path.exists(CADQUERY_SCRIPT_FILE):
    print(f"错误：CadQuery 脚本文件 '{CADQUERY_SCRIPT_FILE}' 未找到。")
    sys.exit(1)

print(f"正在读取并执行 CadQuery 脚本：{CADQUERY_SCRIPT_FILE}")

# 将脚本内容读入字符串
with open(CADQUERY_SCRIPT_FILE, 'r') as f:
    py_string = f.read()

# 执行 py_string，它会把生成的 CadQuery 对象赋值给全局变量 'r'
try:
    exec(py_string, globals())
except Exception as e:
    print(f"执行 CadQuery 脚本时出错：{e}")
    sys.exit(1)

# 确保 'r' 变量已在全局作用域中创建
if 'r' not in globals():
    print(f"错误：CadQuery 脚本 '{CADQUERY_SCRIPT_FILE}' 没有在全局作用域中定义名为 'r' 的变量。")
    print("请确保你的脚本将最终的 CadQuery 对象赋值给 'r'。")
    sys.exit(1)

# 获取 CadQuery 模型对象
compound = globals()['r'].val()
print("CadQuery 模型已成功加载。")

# 2. 网格化并导出 STL 和 STEP 文件
print(f"正在生成 STL 文件到：{output_stl_path}")
print(f"正在生成 STEP 文件到：{output_step_path}")

try:
    # 转换为网格
    vertices, faces = compound.tessellate(0.001, 0.1)
    mesh = trimesh.Trimesh([(v.x, v.y, v.z) for v in vertices], faces)

    # 导出 STL
    mesh.export(output_stl_path)

    # 导出 STEP
    cq.exporters.export(compound, output_step_path)

    print("STL 和 STEP 文件导出完成。")

except Exception as e:
    print(f"导出文件时发生错误：{e}")
    sys.exit(1)

# 3. Open3D 处理（根据你提供的demo，尽管可能不再需要渲染显示）
# 注意：如果你不需要在Python脚本中显示渲染结果，下面的Open3D部分可以省略
try:
    mesh_o3d = o3d.io.read_triangle_mesh(output_stl_path)
    # 你的demo中有缩放操作，这里保留
    mesh_o3d.vertices = o3d.utility.Vector3dVector(np.asarray(mesh_o3d.vertices) / 100.)
    # 你的demo中有颜色设置，这里保留
    mesh_o3d.paint_uniform_color(np.array([255, 255, 136]) / 255)
    mesh_o3d.compute_vertex_normals()

    # 如果你仍然想看到Open3D的交互式窗口，可以取消注释下面这行：
    # o3d.visualization.draw_geometries([mesh_o3d])

    # 你的demo中有matplotlib的render函数，这里无法直接复现
    # 如果 render 函数是你自定义的，你需要确保它在此环境中可用
    # plt.figure(figsize=(3, 3))
    # _ = plt.imshow(render(mesh_o3d))
    # plt.show() # 如果要显示图片，需要这行

except Exception as e:
    print(f"Open3D 处理过程中发生错误（这通常与显示/进一步处理有关，不影响STL生成）：{e}")

print("脚本执行完毕。")