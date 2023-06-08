import os
import shutil

# organizes files in the downloads directory by their file type(ex: pdf, exe, jpg, etc...)


def organize_downloads():
    # Specify the path to the Downloads folder
    downloads_folder = 'C:\\Users\\njdon\\Downloads'

    # Iterate over all files in the Downloads folder
    for filename in os.listdir(downloads_folder):
        # Get the full path of the file
        file_path = os.path.join(downloads_folder, filename)

        # Skip directories/folders
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        file_ext = os.path.splitext(filename)[1]
        file_ext_name = file_ext[1:].upper()

        # create a folder with file extension name
        folder = os.path.join(downloads_folder, file_ext_name)
        if not os.path.exists(folder):
            os.makedirs(folder)

        # move file to the specified folder
        shutil.move(file_path, os.path.join(folder, filename))

        print("ALL ORGANIZED!")


# Call the function to organize the downloads
organize_downloads()
