import os
import shutil





def move_matching_htm_files(full_bible_folder, reference_bible_folder, testerment_folder):
    # Make sure the destination folder exists
    os.makedirs(testerment_folder, exist_ok=True)

    # List all files in the name source folder
    file_names = os.listdir(full_bible_folder)

    for file_name in file_names:
        # Remove the extension from the original file
        base_name, _ = os.path.splitext(file_name)
        reference_file_name = base_name + ".csv"


        # Full path to the .htm file in the reference_bible_folder
        reference_file_path = os.path.join(reference_bible_folder, reference_file_name)
        full_file_path = os.path.join(full_bible_folder, file_name)
        

        # Check if the .htm file exists
        if os.path.isfile(reference_file_path):
            # Move the .htm file to the destination folder
            shutil.move(full_file_path, os.path.join(testerment_folder, file_name))
            print(f"Moved: {file_name}")
        else:
            print(f"Not found: {file_name}")

full_bible_folder = "Englishbible"      
reference_bible_folder = "Giriama_Chapter_csvs"                     
testerment_folder = "Englishbible/New_testerment"      

move_matching_htm_files(full_bible_folder, reference_bible_folder, testerment_folder)




#in case the list needs to be munipulated (ie the names arent the same across folders) you can use this 
def list_files_in_folder(folder_path):
    # Create an empty list to store file names
    file_list = []

    # Loop through each file in the folder
    for file_name in os.listdir(folder_path):
        # Create full path
        full_path = os.path.join(folder_path, file_name)

        # Check if it is a file (not a folder)
        if os.path.isfile(full_path):
            file_list.append(file_name)

    return file_list

# Example usage
folder_path = '/path/to/your/folder'  # Change this to your target folder
files = list_files_in_folder(folder_path)

print("Files in folder:")
print(files)