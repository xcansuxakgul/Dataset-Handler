import argparse
import os
from dataset_handler import find_corrupted_images, reorganize_and_split_dataset, shrink_dataset

def main():
    parser = argparse.ArgumentParser(description="Dataset handler for splitting and reorganizing datasets.")
    
    # Add arguments for finding corrupted images
    parser.add_argument('--find-corrupted', action='store_true', help='Find and list corrupted images.')
    parser.add_argument('--corrupted-output', type=str, default='corrupted_images.txt', help='Output file for corrupted images.')

    # Add arguments for reorganizing and splitting datasets
    parser.add_argument('--reorganize-split', action='store_true', help='Reorganize and split dataset.')
    parser.add_argument('--csv-path', type=str, help='Path to the CSV file containing dataset information.')
    parser.add_argument('--source-dir', type=str, help='Directory containing the source images.')
    parser.add_argument('--target-dir', type=str, help='Directory where the dataset will be organized and split.')
    parser.add_argument('--test-size', type=float, default=0.2, help='Proportion of the dataset to be used as the test set.')
    parser.add_argument('--val-size', type=float, default=0.1, help='Proportion of the dataset to be used as the validation set.')

    # Add arguments for shrinking the dataset
    parser.add_argument('--shrink-dataset', action='store_true', help='Shrink dataset.')
    parser.add_argument('--root-dir', type=str, help='Path to the root dataset directory.')
    parser.add_argument('--percentage', type=float, help='Percentage of the dataset to retain.')
    parser.add_argument('--output-dir', type=str, help='Path to the output directory for the shrunk dataset.')

    args = parser.parse_args()

    # Finding corrupted images
    if args.find_corrupted:
        if os.path.exists(args.source_dir):
            find_corrupted_images(args.source_dir, args.corrupted_output)
            print(f"Corrupted images have been listed in {args.corrupted_output}.")
        else:
            print(f"Source directory {args.source_dir} does not exist. Please provide a valid directory.")
    
    # Reorganizing and splitting dataset
    if args.reorganize_split:
        if all([args.csv_path, args.source_dir, args.target_dir]):
            reorganize_and_split_dataset(
                args.csv_path,
                args.source_dir,
                args.target_dir,
                test_size=args.test_size,
                val_size=args.val_size
            )
            print(f"Dataset has been reorganized and split into {args.target_dir}.")
        else:
            print("Error: --csv-path, --source-dir, and --target-dir are required for dataset reorganization and splitting.")

    # Shrinking the dataset
    if args.shrink_dataset:
        if all([args.root_dir, args.percentage, args.output_dir]):
            shrink_dataset(
                args.root_dir,
                args.percentage,
                args.output_dir
            )
            print(f'Dataset shrunk into {args.output_dir}.')
        else:
            print("Error: --root-dir, --percentage, and --output-dir are required for dataset shrinking.")

if __name__ == '__main__':
    main()