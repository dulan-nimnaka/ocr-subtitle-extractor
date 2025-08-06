import os

""""
01. Setup & Loading Images from a Folder

- Get the folder path from the user.
- List all image files in that folder.
- Handle errors like "folder not found" or "no images".

"""
class OCRProcessor:
    def load_images(folder_path):
        # Check if folder exists
        if not os.path.exists(folder_path):
            raise FileNotFoundError("Folder '{foder_path}' does not exist!")

        # List image files with supported extensions
        supported_ext = ('.jpg', '.jpeg', '.png')
        files = os.listdir(folder_path)
        images = [f for f in files if f.lower().endswith(supported_ext)]

        if not images:
            raise ValueError(f"No images found in folder '{folder_path}'. Please add some .jpg/.jpeg/.png files.")
        
        return images
    
    # Running the step
    try:
        folder = input("Enter image folder path: ").strip()
        image_files = load_images(folder)
        print(f"Found {len(image_files)} image(s): {image_files}")

    except Exception as e:
        print(f"Error: {e}")