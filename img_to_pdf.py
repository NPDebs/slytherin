# Import the sys module
import sys
#  For interacting with the OS; used for file and directory operations.
import os
# Import the img2pdf library, which convert images to PDF format.
import img2pdf

# Retrieves the command-line argument provided when running the script. The first CL arg (index 1) = image file or dir path.
filepath = sys.argv[1]

# To check if the provided path is a directory.
if os.path.isdir(filepath):
    with open("output_image.pdf", "wb") as file:
        imgs = []
        for fname in os.listdir(filepath):
            if not fname.endswith(".jpg"):
                continue
            path = os.path.join(filepath, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        file.write(img2pdf.convert(imgs))

# If the path is not a dir, check if it is a file.
elif os.path.isfile(filepath):
    if filepath.endswith(".jpg"):
        with open("output.pdf", "wb") as file:
            file.write(img2pdf.convert(filepath))

# Print error msg if the provided path is neither a directory nor a file
else:
    print("Please confirm the file or directory inputed.")

# TO-DO: Add condition for .png and other file types