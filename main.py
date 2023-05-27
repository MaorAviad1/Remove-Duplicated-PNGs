Certainly! Here is the annotated script:

```python
# Import required libraries
import os
import shutil
from PIL import Image
from imagehash import phash

# Define function to remove duplicate images
def remove_duplicate_images(dir_path, dump_path):
    # Create dump directory if it doesn't exist
    if not os.path.exists(dump_path):
        os.makedirs(dump_path)

    # Create an empty dictionary to store image hashes
    hash_keys = dict()

    # Get a list of all PNG files in the directory
    image_files = [f for f in os.listdir(dir_path) if f.endswith('.png')]

    # Iterate through each image file
    for index, img in enumerate(image_files):
        try:
            # Open the image file
            with Image.open(dir_path + "/" + img) as im:
                # Calculate the perceptual hash of the image
                h = str(phash(im))
                # If the hash already exists in the dictionary, it's a duplicate
                if h in hash_keys:
                    print(f"Duplicate image: {img} -> Moving to dump folder")
                    # Move duplicate image to the dump directory
                    shutil.move(dir_path + "/" + img, dump_path + "/" + img)
                else:
                    # If the hash is new, add it to the dictionary
                    hash_keys[h] = img
        except Exception as e:
            # Handle any errors during image processing
            print(f"Error: {img}: {e}")

# Define the directory paths
dir_path = 'your_image_directory'
dump_path = 'your_dump_directory'

# Call the function to remove duplicate images
remove_duplicate_images(dir_path, dump_path)
```

Remember to replace `'your_image_directory'` and `'your_dump_directory'` with the paths to the directories you're using before running the script.