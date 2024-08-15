import unittest
import os
import shutil
from PIL import Image
from dataset_handler import find_corrupted_images, reorganize_and_split_dataset

class TestDatasetHandler(unittest.TestCase):

    # Define constants for file and directory paths
    TEST_DIR = 'test_data/'
    OUTPUT_FILE = 'test_corrupted_images.txt'
    CSV_PATH = 'test_train.csv'
    SOURCE_DIR = os.path.join(TEST_DIR, 'train/')
    TARGET_DIR = os.path.join(TEST_DIR, 'data/train/')

    def setUp(self):
        # Set up the directories and files for testing
        self._create_directories()
        self._create_fake_images()
        self._create_csv_file()

    def _create_directories(self):
        # Create directories for testing
        os.makedirs(self.SOURCE_DIR, exist_ok=True)
        os.makedirs(self.TARGET_DIR, exist_ok=True)

    def _create_fake_images(self):
        # Create a few valid and invalid images
        valid_image_path = os.path.join(self.SOURCE_DIR, 'valid_image.jpg')
        invalid_image_path = os.path.join(self.SOURCE_DIR, 'invalid_image.jpg')

        # Create a valid image
        Image.new('RGB', (100, 100)).save(valid_image_path)

        # Create an invalid image (corrupted image)
        with open(invalid_image_path, 'w') as f:
            f.write("This is not a valid image file.")

    def _create_csv_file(self):
        # Create a CSV file for testing
        csv_content = 'id,prediction\nvalid_image.jpg,1\ninvalid_image.jpg,0\n'
        with open(self.CSV_PATH, 'w') as f:
            f.write(csv_content)

    def test_find_corrupted_images(self):
        # Test finding corrupted images
        find_corrupted_images(self.SOURCE_DIR, self.OUTPUT_FILE)

        # Check if the output file has the corrupted image path
        with open(self.OUTPUT_FILE, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 1)
            self.assertIn('invalid_image.jpg', lines[0])

    def test_reorganize_and_split_dataset(self):
        # Test the reorganization and splitting of the dataset
        reorganize_and_split_dataset(self.CSV_PATH, self.SOURCE_DIR, self.TARGET_DIR, test_size=0.5, val_size=0.25)

        # Check if the files are moved to the correct directories
        for split in ['train', 'val', 'test']:
            split_dir = os.path.join(self.TARGET_DIR, split)
            self.assertTrue(os.path.exists(split_dir))
            for img_id in os.listdir(split_dir):
                self.assertIn(img_id, ['valid_image.jpg', 'invalid_image.jpg'])

    def tearDown(self):
        # Clean up the directories and files after testing
        shutil.rmtree(self.TEST_DIR)
        if os.path.exists(self.OUTPUT_FILE):
            os.remove(self.OUTPUT_FILE)
        if os.path.exists(self.CSV_PATH):
            os.remove(self.CSV_PATH)

if __name__ == '__main__':
    unittest.main()