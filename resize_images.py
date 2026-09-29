import os
from PIL import Image

def resize_images(folder_path, max_dimension=1200):
    for filename in os.listdir(folder_path):
        if filename.endswith(".webp"):
            filepath = os.path.join(folder_path, filename)
            
            try:
                with Image.open(filepath) as img:
                    # If it's the hero image, allow a larger dimension
                    current_max = 1920 if "hero" in filename.lower() else max_dimension
                    
                    if img.width > current_max or img.height > current_max:
                        # Resize preserving aspect ratio
                        img.thumbnail((current_max, current_max), Image.Resampling.LANCZOS)
                        img.save(filepath, 'webp', quality=75)
                        print(f"Resized {filename} to {img.size}")
                    else:
                        print(f"Skipped {filename} (already small enough)")
            except Exception as e:
                print(f"Error resizing {filename}: {e}")

if __name__ == '__main__':
    images_dir = r"e:\Downloads\saloon\images"
    resize_images(images_dir)
