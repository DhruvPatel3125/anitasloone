import os
import sys

try:
    from PIL import Image
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

def convert_to_webp(folder_path):
    print(f"Processing folder: {folder_path}")
    if not os.path.exists(folder_path):
        print("Folder does not exist")
        return

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg.jpg") or filename.endswith(".jpg") or filename.endswith(".png"):
            filepath = os.path.join(folder_path, filename)
            # Create new filename by replacing extension
            base_name = filename.replace('.jpg.jpg', '').replace('.jpg', '').replace('.png', '')
            new_filename = f"{base_name}.webp"
            new_filepath = os.path.join(folder_path, new_filename)
            
            try:
                with Image.open(filepath) as img:
                    # Convert to webp with reduced quality (e.g., 70-80) to save space
                    # The default quality is usually 80, we can use 75
                    img.save(new_filepath, 'webp', quality=75)
                    print(f"Converted {filename} -> {new_filename}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

if __name__ == '__main__':
    images_dir = r"e:\Downloads\saloon\images"
    convert_to_webp(images_dir)
