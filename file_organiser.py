# Import tools to work with files and folders
import os
import shutil

# Define function, passing it starting and destination folders as arguments
def organise_files(starting_folder, destination_folder):
    # Check if destination exists and create if it doesn't
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Check if the starting folder exists
    if not os.path.exists(starting_folder):
        print(f"The starting folder '{starting_folder}' does not exist.")
        return

    # Make a list of files in the starting_folder and store in "files"
    files = os.listdir(starting_folder)
    print(files)

    # Loop through the list of files and extract file path
    for file in files:
        starting_path = os.path.join(starting_folder, file)
        # print(starting_path)

        # Check if file is an actual file and not a directory
        if os.path.isfile(starting_path):
            # Get the file extension
            _, extension = os.path.splitext(file)  # Extract the file extension
            # print(extension)
            
            # Create new folder(s) for each file type
            extension_folder = os.path.join(destination_folder, extension[1:])
            
            # If the new folder doesn't exist, then create it
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            # Move file to the corresponding folder
            destination_path = os.path.join(extension_folder, file)
            shutil.move(starting_path, destination_path)
            print(f"{file} has been moved to {extension_folder}")

# Prompt user to enter the current folder path and new desired location
starting_folder = input("Enter path of folder you want to clean up: ")
destination_folder = input("Enter path of folder where you want files to be: ")

organise_files(starting_folder, destination_folder)

# TO-DO: Write a second function which reverses this action. Allow user decide which function to perform.
