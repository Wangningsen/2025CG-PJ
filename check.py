import os
import re

def check_winner_loser_correspondence(gt_dir, cadquery_dir):
    """
    检查 ground_truth 目录中的每个 GT 脚本是否有对应的 winner 和 loser 脚本在 cadquery 目录中。

    Args:
        gt_dir (str): ground_truth 脚本的目录路径。
        cadquery_dir (str): winner 和 loser 脚本的目录路径。
    """

    print(f"开始检查文件对应关系...\nGround Truth 目录: {gt_dir}\nCadQuery 目录: {cadquery_dir}\n")

    missing_winner_count = 0
    missing_loser_count = 0
    total_gt_files = 0
    checked_uuids = set()

    # 遍历 ground_truth 目录
    for filename in os.listdir(gt_dir):
        if not filename.endswith(".py"):
            continue

        total_gt_files += 1
        gt_file_path = os.path.join(gt_dir, filename)

        # 提取 UUID。假设 GT 文件名格式为 "uuid.py"
        uuid = os.path.splitext(filename)[0]
        
        # 避免重复检查同一个 UUID（如果文件名有其他变种）
        if uuid in checked_uuids:
            continue
        checked_uuids.add(uuid)

        winner_file_name = f"{uuid}_winner.py"
        loser_file_name = f"{uuid}_loser.py"

        winner_file_path = os.path.join(cadquery_dir, winner_file_name)
        loser_file_path = os.path.join(cadquery_dir, loser_file_name)

        has_winner = os.path.isfile(winner_file_path)
        has_loser = os.path.isfile(loser_file_path)

        if not has_winner or not has_loser:
            print(f"UUID: {uuid} 存在问题:")
            if not has_winner:
                print(f"  - 缺少 Winner 脚本: {winner_file_name}")
                missing_winner_count += 1
            if not has_loser:
                print(f"  - 缺少 Loser 脚本: {loser_file_name}")
                missing_loser_count += 1
            print("-" * 30)

    print(f"\n检查完成。")
    print(f"共检查了 {total_gt_files} 个 GT 文件。")
    print(f"缺少 Winner 脚本的 GT 数量: {missing_winner_count}")
    print(f"缺少 Loser 脚本的 GT 数量: {missing_loser_count}")

    if missing_winner_count == 0 and missing_loser_count == 0:
        print("\n**所有 Ground Truth 文件都有对应的 Winner 和 Loser 脚本。**")
    else:
        print("\n**发现部分 Ground Truth 文件缺少对应的 Winner 或 Loser 脚本。请检查上述列表。**")

if __name__ == "__main__":
    # 定义你的目录路径
    ground_truth_directory = "/home/user2/wns/cad-recode/dpo_data/ground_truth"
    cadquery_directory = "/home/user2/wns/cad-recode/dpo_data/cadquery"

    # 执行检查
    check_winner_loser_correspondence(ground_truth_directory, cadquery_directory)