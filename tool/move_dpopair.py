import os
import shutil
import re

def organize_cadquery_data(source_dir, target_cadquery_dir, target_ground_truth_dir):
    """
    遍历源目录中的 CadQuery 脚本文件，并根据其类型移动到目标目录。

    Args:
        source_dir (str): 包含 winner, loser, gt 脚本的源目录路径。
        target_cadquery_dir (str): 存放 winner 和 loser 脚本的目标目录路径。
        target_ground_truth_dir (str): 存放 gt 脚本的目标目录路径。
    """

    # 确保目标目录存在，如果不存在则创建
    os.makedirs(target_cadquery_dir, exist_ok=True)
    os.makedirs(target_ground_truth_dir, exist_ok=True)

    print(f"开始整理文件...\n源目录: {source_dir}\n目标 CadQuery 目录: {target_cadquery_dir}\n目标 Ground Truth 目录: {target_ground_truth_dir}\n")

    # 用于匹配文件名的正则表达式
    # 捕获 UUID 部分
    gt_pattern = re.compile(r"(.+)_gt_code\.py$")
    winner_pattern = re.compile(r"(.+)_winner\.py$")
    loser_pattern = re.compile(r"(.+)_loser\.py$")

    moved_count = 0
    skipped_count = 0

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path):
            # 检查是否是 GT 文件
            match_gt = gt_pattern.match(filename)
            if match_gt:
                uuid = match_gt.group(1)
                new_filename = f"{uuid}.py" # GT 文件通常无需改名，但为了后续使用，统一为.py
                destination_path = os.path.join(target_ground_truth_dir, new_filename)
                try:
                    shutil.move(file_path, destination_path)
                    print(f"移动 GT: {filename} -> {destination_path}")
                    moved_count += 1
                except Exception as e:
                    print(f"移动 GT 文件 {filename} 失败: {e}")
                continue # 处理完一个文件就跳到下一个

            # 检查是否是 Winner 文件
            match_winner = winner_pattern.match(filename)
            if match_winner:
                uuid = match_winner.group(1)
                new_filename = f"{uuid}_winner.py" # 保持原名
                destination_path = os.path.join(target_cadquery_dir, new_filename)
                try:
                    shutil.move(file_path, destination_path)
                    print(f"移动 Winner: {filename} -> {destination_path}")
                    moved_count += 1
                except Exception as e:
                    print(f"移动 Winner 文件 {filename} 失败: {e}")
                continue

            # 检查是否是 Loser 文件
            match_loser = loser_pattern.match(filename)
            if match_loser:
                uuid = match_loser.group(1)
                new_filename = f"{uuid}_loser.py" # 保持原名
                destination_path = os.path.join(target_cadquery_dir, new_filename)
                try:
                    shutil.move(file_path, destination_path)
                    print(f"移动 Loser: {filename} -> {destination_path}")
                    moved_count += 1
                except Exception as e:
                    print(f"移动 Loser 文件 {filename} 失败: {e}")
                continue

            # 如果文件不符合任何模式
            print(f"跳过文件（不符合命名模式）: {filename}")
            skipped_count += 1

    print(f"\n文件整理完成。")
    print(f"成功移动文件: {moved_count} 个")
    print(f"跳过文件: {skipped_count} 个 (不符合命名模式或已处理)")

if __name__ == "__main__":
    # 定义源目录和目标目录
    source_directory = "/home/user2/wns/cad-recode/cad-recode-v1.5-data-origindpo/dpo_preference_pairs_best_median/train/"
    target_cadquery_directory = "/home/user2/wns/cad-recode/dpo_data/cadquery"
    target_ground_truth_directory = "/home/user2/wns/cad-recode/dpo_data/ground_truth"

    # 执行文件整理
    organize_cadquery_data(source_directory, target_cadquery_directory, target_ground_truth_directory)

    # 提示用户下一步可以做的工作
    print("\n--- 下一步建议 ---")
    print(f"1. 你可以检查一下目标目录：")
    print(f"   - {target_cadquery_directory}")
    print(f"   - {target_ground_truth_directory}")
    print("2. 确认 `ground_truth` 目录中的 `_gt_code.py` 文件是否需要被重命名为 `_winner.py` (如果它们本身就是最终 GT 的话) 或者你需要调整你的数据集加载逻辑。")
    print("   如果你打算让 `_winner.py` **既是** DPO 的 chosen 脚本，**又是** 用于生成点云的 GT 脚本，那么你需要将 `dpo_data/ground_truth/` 下的 `uuid.py` 文件复制或移动到 `dpo_data/cadquery/` 目录下，并重命名为 `uuid_winner.py` (如果它们还没有被命名为 `uuid_winner.py`)。")
    print("   **或者，更推荐的方式是：在你的 `Fusion360DPODataset` 中，直接使用 `uuid_winner.py` 作为 `gt_cadquery_path` 来生成点云，而不是 `ground_truth` 目录下的文件。**")
    print("   这样，`dpo_data/ground_truth` 目录可能就不是必要的，除非你有其他用途。")
    print("3. 接下来，你需要运行**预处理脚本**，根据 `dpo_data/cadquery/` 中的 `_winner.py` 文件来生成 `dpo_data/reconstruction/` 目录下的 `.stl` 文件。")
    print("4. 最后，创建或更新 `dpo_data/train_val.json` 文件，包含你的 UUID 列表。")