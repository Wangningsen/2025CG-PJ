import os
import sys
import cadquery as cq
import trimesh
import open3d as o3d # 不需要导入，除非你打算在脚本中进行Open3D的可视化或处理
import numpy as np # trimesh 和 cadquery 内部会处理 numpy，这里不需要显式导入

def convert_cadquery_gt_to_stl(source_gt_dir, target_reconstruction_dir):
    """
    遍历源目录中的 CadQuery GT 脚本，执行它们并生成对应的 STL 文件到目标目录。

    Args:
        source_gt_dir (str): 存放 CadQuery GT 脚本的源目录路径。
        target_reconstruction_dir (str): 存放生成的 STL 文件的目标目录路径。
    """

    # 确保目标目录存在，如果不存在则创建
    os.makedirs(target_reconstruction_dir, exist_ok=True)

    print(f"开始将 CadQuery GT 脚本转换为 STL 文件...\n源目录: {source_gt_dir}\n目标目录: {target_reconstruction_dir}\n")

    processed_count = 0
    failed_count = 0

    # 遍历源目录中的所有文件
    for filename in os.listdir(source_gt_dir):
        # 只处理以 .py 结尾的文件
        if not filename.endswith(".py"):
            print(f"跳过非 Python 文件: {filename}")
            continue

        gt_script_path = os.path.join(source_gt_dir, filename)
        # 假设 GT 脚本的文件名是 uuid.py，那么 STL 文件的名称就是 uuid.stl
        uuid = os.path.splitext(filename)[0] # 获取不带扩展名的文件名作为 UUID
        output_stl_path = os.path.join(target_reconstruction_dir, f"{uuid}.stl")

        # 检查 STL 文件是否已经存在，如果存在则跳过以避免重复生成
        if os.path.exists(output_stl_path):
            print(f"STL 文件已存在: {output_stl_path}. 跳过 {filename}")
            processed_count += 1
            continue

        print(f"正在处理脚本: {filename}")

        # 1. 读取 CadQuery 脚本内容
        try:
            with open(gt_script_path, 'r') as f:
                py_string = f.read()
        except Exception as e:
            print(f"错误: 读取脚本 {filename} 失败: {e}")
            failed_count += 1
            continue

        # 使用一个独立的字典作为 exec 的全局命名空间，以隔离脚本执行
        exec_globals = {'cq': cq}
        try:
            # 执行 py_string，它会把生成的 CadQuery 对象赋值给 exec_globals['r']
            exec(py_string, exec_globals)
        except Exception as e:
            print(f"错误: 执行 CadQuery 脚本 {filename} 时出错: {e}")
            failed_count += 1
            continue

        # 确保 'r' 变量已在执行脚本的命名空间中创建
        if 'r' not in exec_globals:
            print(f"错误: 脚本 '{filename}' 没有在全局作用域中定义名为 'r' 的变量。跳过。")
            failed_count += 1
            continue

        # 获取 CadQuery 模型对象
        try:
            # 根据你提供的逻辑，使用 .val() 获取实际的 OCC Compound 或 Shape
            compound = exec_globals['r'].val()
            if not isinstance(compound, (cq.Workplane, cq.Shape)):
                print(f"警告: 脚本 '{filename}' 中的 'r' 不是一个 Workplane 或 Shape 对象。尝试直接使用 'r'。")
                compound = exec_globals['r'] # 尝试直接使用 r
                if not isinstance(compound, (cq.Workplane, cq.Shape)):
                     print(f"错误: 脚本 '{filename}' 中的 'r' 既不是 Workplane 也不是 Shape。跳过。")
                     failed_count += 1
                     continue
        except Exception as e:
            print(f"错误: 获取 CadQuery 模型对象失败 {filename}: {e}")
            failed_count += 1
            continue

        # 2. 网格化并导出 STL 文件
        try:
            # 根据你提供的逻辑，使用 tessellate
            vertices, faces = compound.tessellate(0.001, 0.1)
            # 你的例子中将 Tessellated vertices 转换为 (x,y,z) 元组列表，trimesh 也可以直接接受 numpy 数组
            mesh = trimesh.Trimesh(vertices=np.array([(v.x, v.y, v.z) for v in vertices]), faces=np.array(faces))

            # 导出 STL
            mesh.export(output_stl_path)
            print(f"成功生成 STL: {output_stl_path}")
            processed_count += 1

        except Exception as e:
            print(f"错误: 导出 STL 文件 {output_stl_path} 失败: {e}")
            failed_count += 1
            continue

    print(f"\nSTL 文件生成完成。")
    print(f"成功处理脚本: {processed_count} 个")
    print(f"失败脚本: {failed_count} 个")

if __name__ == "__main__":
    # 定义源目录和目标目录
    source_gt_directory = "/home/user2/wns/cad-recode/dpo_data/ground_truth"
    target_reconstruction_directory = "/home/user2/wns/cad-recode/dpo_data/reconstruction"

    # 执行转换
    convert_cadquery_gt_to_stl(source_gt_directory, target_reconstruction_directory)

    print("\n--- 后续步骤提醒 ---")
    print("1. 现在 `dpo_data/reconstruction/` 目录下应该有了所有对应的 `.stl` 文件。")
    print("2. 你需要确保 `dpo_data/cadquery/` 目录中的 `_winner.py` 文件是你的 `GT` CadQuery 脚本的副本（或者就是 GT 脚本本身）。因为在训练中，`_winner.py` 既是模型的 `chosen` 响应，也应是你用于生成点云的源代码。")
    print("   **请注意：** 如果你的 `_gt_code.py` 是最准确的 GT，并且你已经把它移动到了 `dpo_data/ground_truth/`，那么为了训练的正确性，你可能需要将这些 `uuid.py` 文件复制到 `dpo_data/cadquery/` 目录下，并确保它们被命名为 `uuid_winner.py`。")
    print("3. 最后，创建或更新 `dpo_data/train_val.json` 文件，包含你所有 UUID 的训练集和验证集划分。")