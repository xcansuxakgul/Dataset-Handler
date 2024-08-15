import os
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(csv_path, test_size=0.2, val_size=0.1, random_state=42):
    df = pd.read_csv(csv_path)
    train_val_df, test_df = train_test_split(
        df, test_size=test_size, stratify=df['prediction'], random_state=random_state
    )
    val_relative_size = val_size / (1 - test_size)
    train_df, val_df = train_test_split(
        train_val_df, test_size=val_relative_size, stratify=train_val_df['prediction'], random_state=random_state
    )
    return train_df, val_df, test_df

def move_files(df, source_dir, target_dir):
    for _, row in df.iterrows():
        img_id = row['id']
        prediction = str(row['prediction'])
        source_img_path = os.path.join(source_dir, img_id)
        target_class_dir = os.path.join(target_dir, prediction)
        os.makedirs(target_class_dir, exist_ok=True)
        if os.path.exists(source_img_path):
            shutil.move(source_img_path, os.path.join(target_class_dir, img_id))
        else:
            print(f"Image {img_id} not found in {source_dir}")

def reorganize_and_split_dataset(csv_path, source_dir, target_dir, test_size=0.2, val_size=0.1):
    train_df, val_df, test_df = split_dataset(csv_path, test_size, val_size)
    splits = {'train': train_df, 'val': val_df, 'test': test_df}
    for split, df in splits.items():
        split_dir = os.path.join(target_dir, split)
        move_files(df, source_dir, split_dir)