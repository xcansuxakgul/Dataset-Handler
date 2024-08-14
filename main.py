import os
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(csv_path, test_size=0.2, val_size=0.1, random_state=42):
    """
    Splits the dataset into training, validation, and test sets.

    Parameters:
    - csv_path (str): Path to the CSV file containing the dataset information.
    - test_size (float): Proportion of the dataset to be used as the test set.
    - val_size (float): Proportion of the dataset to be used as the validation set.
    - random_state (int): Seed used by the random number generator for reproducibility.

    Returns:
    - train_df (DataFrame): Training set DataFrame.
    - val_df (DataFrame): Validation set DataFrame.
    - test_df (DataFrame): Test set DataFrame.
    """
    # Read the dataset from the CSV file
    df = pd.read_csv(csv_path)
    
    # Split the dataset into training+validation and test sets
    train_val_df, test_df = train_test_split(
        df, test_size=test_size, stratify=df['prediction'], random_state=random_state
    )
    
    # Calculate the relative size of the validation set within the training+validation set
    val_relative_size = val_size / (1 - test_size)
    
    # Further split the training+validation set into training and validation sets
    train_df, val_df = train_test_split(
        train_val_df, test_size=val_relative_size, stratify=train_val_df['prediction'], random_state=random_state
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
        
        # Define the source and target paths for the image
        source_img_path = os.path.join(source_dir, img_id)
        target_class_dir = os.path.join(target_dir, prediction)
        
        # Create the target directory if it doesn't exist
        os.makedirs(target_class_dir, exist_ok=True)
        
        # Move the image if it exists, otherwise print a warning
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
    # Split the dataset into training, validation, and test sets
    train_df, val_df, test_df = split_dataset(csv_path, test_size, val_size)
    
    # Dictionary to map each split to its corresponding DataFrame
    splits = {'train': train_df, 'val': val_df, 'test': test_df}
    
    # Move the files for each split
    for split, df in splits.items():
        split_dir = os.path.join(target_dir, split)
        move_files(df, source_dir, split_dir)

if __name__ == "__main__":
    csv_path = 'train.csv'
    source_dir = 'train/train'
    target_dir = 'data/train'
    
    # Execute the reorganization and dataset splitting process
    reorganize_and_split_dataset(csv_path, source_dir, target_dir, test_size=0.2, val_size=0.1)
