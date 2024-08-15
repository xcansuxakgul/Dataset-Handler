from PIL import Image
import os

def find_corrupted_images(directory, output_file):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                try:
                    img = Image.open(file_path)
                    img.verify()
                except (IOError, SyntaxError) as e:
                    print(f"Corrupted image found: {file_path}")
                    file.write(file_path + '\n')