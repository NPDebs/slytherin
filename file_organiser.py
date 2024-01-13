# Import tools to work with files and folders
import os
import shutil

# Define function, passing it starting and destination folders as arguments
def organise_files(starting_folder, destination_folder):
    # Check if destination exists and create if it doesn't
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Make a list of files in the starting_folder and store in "files"
    files = os.listdir(starting_folder)
    print(files)

    # Loop through the list of files and extract 
    for file in files:
        starting_path = os.path.join(starting_folder, file)
        print(starting_path)
