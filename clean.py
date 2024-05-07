import os
import shutil
import json

# Function to load file type mappings from JSON file
def load_file_types_mapping(json_file):
    with open(json_file) as f:
        return json.load(f)

# Function to move files to appropriate folders
def organize_downloads(downloads_dir, file_types_mapping):
    for filename in os.listdir(downloads_dir):
        if os.path.isfile(os.path.join(downloads_dir, filename)):
            file_ext = filename.split('.')[-1].lower()
            for folder, extensions in file_types_mapping.items():
                if file_ext in extensions:
                    folder_path = os.path.join(downloads_dir, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(os.path.join(downloads_dir, filename), os.path.join(folder_path, filename))
                    break  # Stop iterating once the file is moved
            else:
                # If file doesn't match any known type, move it to a generic folder
                generic_folder = os.path.join(downloads_dir, "Miscellaneous")
                if not os.path.exists(generic_folder):
                    os.makedirs(generic_folder)
                shutil.move(os.path.join(downloads_dir, filename), os.path.join(generic_folder, filename))

# Function to delete empty directories in downloads folder
def delete_empty_directories(downloads_dir):
    for root, dirs, files in os.walk(downloads_dir, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):  # If directory is empty
                os.rmdir(dir_path)

# Example usage
downloads_directory = "/home/kryptokazz/Downloads"
file_types_mapping = load_file_types_mapping("file_types_mapping.json")
organize_downloads(downloads_directory, file_types_mapping)
delete_empty_directories(downloads_directory)

