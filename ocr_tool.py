import os
from PIL import Image, ImageOps # used to import the Image and ImageOps modules from the Python Imaging Library (Pillow).


class OCRProcessor:

    """"
    01. Setup & Loading Images from a Folder

    - Get the folder path from the user.
    - List all image files in that folder.
    - Handle errors like "folder not found" or "no images".

    """
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
    
    '''
    # ============Running the step
    try:
        folder = input("Enter image folder path: ").strip()
        image_files = load_images(folder)
        print(f"Found {len(image_files)} image(s): {image_files}")

    except Exception as e:
        print(f"Error: {e}")'''

    """"
    02. Opening & Preprocessing Images (Grayscale)

    - Open images safely using Pillow (PIL).
    - Convert them to grayscale for better OCR accuracy.
    - Handle common errors like corrupted or unreadable files.

    """
    '''
    def preprocess_image(image_path):
        try:
            # Open image safely
            with Image.open(image_path) as img:
                # Convert to grayscale
                grey_img = ImageOps.grayscale(img)
                return grey_img
            
        except FileNotFoundError:
            print(f"❌ File not found: {image_path}")
            return None
        
        except OSError:
            # Raised if file is not an image or is corrupted
            print(f"❌ Cannot open image (corrupted or invalid): {image_path}")
            return None
        
        # ============Running the step
        folder = input("Enter image folder path: ").strip()
        try:
            image_files = load_images(folder) #01
            for img_name in image_files:
                path = os.path.join(folder, img_name)
                grey_img = preprocess_image(image_path)

                if grey_img:
                    grey_img.show() # Opens image viewer (for testing)
                    print(f"Preprocessed {img_name}")
        except Exception as e:
            print(f"Error: {e}")
    '''

    """
    03. Extracting Text with pytesseract

    - Load each preprocessed (grayscale) image.
    - Extract text using pytesseract.
    - Handle unreadable/blank text.

    """




        




    




    