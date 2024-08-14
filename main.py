import os
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split
import argparse

def split_dataset(csv_path, test_size=0.2, val_size=0.1):
    """
    Splits the dataset into training, validation, and test sets.

    Parameters:
    - csv_path (str): Path to the CSV file containing the dataset information.
    - test_size (float): Proportion of the dataset to be used as the test set.
    - val_size (float): Proportion of the dataset to be used as the validation set.

    Returns:
    - train_df (DataFrame): Training set DataFrame.
    - val_df (DataFrame): Validation set DataFrame.
    - test_df (DataFrame): Test set DataFrame.
    """
    df = pd.read_csv(csv_path)
    train_val_df, test_df = train_test_split(
        df, test_size=test_size
    )
    val_relative_size = val_size / (1 - test_size)
    train_df, val_df = train_test_split(
        train_val_df, test_size=val_relative_size
    )
    return train_df, val_df, test_df

def move_files(df, source_dir, target_dir):
    """
    Moves image files from the source directory to the target directory based on class labels.

    Parameters:
    - df (DataFrame): DataFrame containing image IDs and their corresponding class labels.
    - source_dir (str): Directory containing the original images.
    - target_dir (str): Directory to which images will be moved, organized by class label.
    """
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
    """
    Splits the dataset and reorganizes the image files into train, validation, and test directories.

    Parameters:
    - csv_path (str): Path to the CSV file containing the dataset information.
    - source_dir (str): Directory containing the original images.
    - target_dir (str): Base directory where the train, validation, and test directories will be created.
    - test_size (float): Proportion of the dataset to be used as the test set.
    - val_size (float): Proportion of the dataset to be used as the validation set.
    """
    train_df, val_df, test_df = split_dataset(csv_path, test_size, val_size)
    splits = {'train': train_df, 'val': val_df, 'test': test_df}
    for split, df in splits.items():
        split_dir = os.path.join(target_dir, split)
        move_files(df, source_dir, split_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split and reorganize dataset.")
    parser.add_argument('csv_path', type=str, help="Path to the CSV file containing the dataset information.")
    parser.add_argument('source_dir', type=str, help="Directory containing the original images.")
    parser.add_argument('target_dir', type=str, help="Base directory where the train, validation, and test directories will be created.")
    parser.add_argument('--test_size', type=float, default=0.2, help="Proportion of the dataset to be used as the test set.")
    parser.add_argument('--val_size', type=float, default=0.1, help="Proportion of the dataset to be used as the validation set.")

    args = parser.parse_args()

    reorganize_and_split_dataset(
        csv_path=args.csv_path,
        source_dir=args.source_dir,
        target_dir=args.target_dir,
        test_size=args.test_size,
        val_size=args.val_size
    )
