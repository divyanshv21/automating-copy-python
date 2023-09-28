import os
import shutil

def copy_files_by_extension(source_folder, destination_folder, file_extension):
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        for foldername, subfolders, filenames in os.walk(source_folder):
            for filename in filenames:
                if filename.endswith(file_extension):
                    source_path = os.path.join(foldername, filename)
                    destination_path = os.path.join(destination_folder, filename)
                    shutil.copy(source_path, destination_path)
                    print(f"Copied: {filename} from {source_path} to {destination_path}")
        print("Copy operation completed")
    except Exception as e:
        print(f"An error occured: {str(e)}")

source_folder = "/your/path/to/source_folder" 
destination_folder = "/your/path/to/destination_folder" 
file_extension = ".pdf"  

# Call the function to copy files by extension
copy_files_by_extension(source_folder, destination_folder, file_extension)
