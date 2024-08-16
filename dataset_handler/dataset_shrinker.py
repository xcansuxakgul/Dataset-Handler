import os
import shutil
import random
from pathlib import Path

def shrink_dataset(root_dir, percentage, output_dir):
    """
    Shrink the dataset by a specified percentage.

    Parameters:
    - root_dir: str, path to the root dataset directory (e.g., 'data/train')
    - percentage: float, percentage of the dataset to retain (e.g., 50.0 for 50%)
    - output_dir: str, path to the output directory where the shrunk dataset will be saved
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for split in ['train', 'val', 'test']:
        split_path = Path(root_dir) / split
        output_split_path = Path(output_dir) / split
        if not os.path.exists(output_split_path):
            os.makedirs(output_split_path)

        for class_dir in os.listdir(split_path):
            class_path = split_path / class_dir
            output_class_path = output_split_path / class_dir
            if not os.path.exists(output_class_path):
                os.makedirs(output_class_path)

            images = [f for f in os.listdir(class_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
            num_images = len(images)
            num_to_keep = int(num_images * (percentage / 100.0))
            selected_images = random.sample(images, num_to_keep)

            for image in selected_images:
                src_path = class_path / image
                dst_path = output_class_path / image
                shutil.copy(src_path, dst_path)
                print(f"Copied {src_path} to {dst_path}")