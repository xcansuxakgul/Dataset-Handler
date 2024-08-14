# Dataset Splitter and Reorganizer

This project is designed to split a dataset into training, validation, and test sets and reorganize image files based on their class labels. The split proportions for each subset can be customized, and the images are moved into corresponding directories for easy access during model training and evaluation. This library used for especially classification tasks with state-of-arts model such as YOLOv8.

## Features

- **Split Dataset**: Splits the dataset into training, validation, and test sets using customizable proportions.
- **Reorganize Files**: Moves image files into directories based on their class labels and subsets (train, val, test).
- **Error Handling**: Notifies the user if an image file is missing during the moving process.

## Prerequisites

You can install the required libraries using the following command:

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
    - Modify the script's parameters (such as `csv_path`, `source_dir`, and `target_dir`) as needed.
    - Execute the script:

    ```bash
    python main.py
    ```

4. **Output**:
    - The script will create `train`, `val`, and `test` directories within the specified `target_dir`, organizing images into subdirectories based on their class labels.

## Example

### Directory Structure

Before running the script:

```
project/
│
├── train.csv
└── train/
    └── train/
        ├── img1.jpg
        ├── img2.jpg
        ├── ...
```

After running the script:

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

## Customization

- **Test and Validation Sizes**:
    - Adjust the `test_size` and `val_size` parameters to control the proportion of the dataset allocated to each subset.
- **Random State**:
    - The `random_state` parameter ensures reproducibility. Modify this if needed for different splits.

## Contributing

If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
