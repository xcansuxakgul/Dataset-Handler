Here’s an updated `README` file incorporating the dataset shrinking feature:

---

# Dataset Splitter, Reorganizer, and Shrinker

This project is designed to split a dataset into training, validation, and test sets, reorganize image files based on their class labels, and shrink the dataset by a specified percentage. The proportions for each subset can be customized, and the images are moved into corresponding directories for easy access during model training and evaluation. This library is particularly useful for classification tasks with state-of-the-art models such as YOLOv8.

## Features

- **Split Dataset**: Splits the dataset into training, validation, and test sets using customizable proportions.
- **Reorganize Files**: Moves image files into directories based on their class labels and subsets (train, val, test).
- **Shrink Dataset**: Reduces the dataset size by a specified percentage, retaining a subset of images.
- **Error Handling**: Notifies the user if an image file is missing during the moving process.
- **Corrupted Image Detection**: Identifies and logs corrupted images in the dataset.

## Prerequisites

Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare Your Dataset**:
    - Ensure your dataset is in a CSV file format with at least two columns:
        - `id`: The unique identifier for each image file.
        - `prediction`: The class label for each image.

2. **Directory Structure**:
    - Place your images in a source directory (e.g., `train/`) corresponding to the image IDs listed in the CSV file.

3. **Run the Script**:
    - Modify the script's parameters (such as `csv_path`, `source_dir`, `target_dir`, and `percentage`) as needed.
    - Execute the script with the appropriate command-line arguments:

    ```bash
    python main.py --reorganize-split --csv-path your_csv_path --source-dir your_source_dir --target-dir your_target_dir --test-size 0.2 --val-size 0.1
    ```

    To shrink the dataset:

    ```bash
    python main.py --shrink-dataset --root-dir your_root_dir --percentage 50.0 --output-dir your_output_dir
    ```

4. **Output**:
    - For reorganizing and splitting: The script will create `train`, `val`, and `test` directories within the specified `target_dir`, organizing images into subdirectories based on their class labels.
    - For shrinking: The script will create a shrunk dataset in the specified `output_dir`, retaining the percentage of images you specified.

## Example

### Directory Structure

**Before running the script:**

```
project/
│
├── train.csv
└── train/
    ├── img1.jpg
    ├── img2.jpg
    ├── ...
```

**After running the script for splitting and reorganizing:**

```
project/
│
├── train.csv
└── data/
    └── train/
        ├── train/
        │   ├── class1/
        │   │   ├── img1.jpg
        │   │   ├── ...
        │   ├── class2/
        │   │   ├── ...
        ├── val/
        │   ├── class1/
        │   │   ├── img3.jpg
        │   │   ├── ...
        └── test/
            ├── class1/
            │   ├── img4.jpg
            │   ├── ...
```

**After running the script for shrinking:**

```
project/
│
├── train.csv
└── data/
    └── shrunk/
        ├── class1/
        │   ├── img1.jpg
        │   ├── ...
        └── class2/
            ├── img2.jpg
            ├── ...
```

## Customization

- **Test and Validation Sizes**:
    - Adjust the `test_size` and `val_size` parameters to control the proportion of the dataset allocated to each subset.
- **Shrink Percentage**:
    - Adjust the `percentage` parameter to specify the proportion of the dataset to retain.
- **Random State**:
    - The `random_state` parameter ensures reproducibility. Modify this if needed for different splits.

## Contributing

If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

Feel free to modify the paths, filenames, or descriptions as needed to fit your project's specific details.
