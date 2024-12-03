import os
import shutil

def organize_files(directory):
    # Change to the specified directory
    os.chdir(directory)

    # Create a list of file extensions and their corresponding folders
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Music': ['.mp3', '.wav'],
        'Archives': ['.zip', '.tar', '.gz'],
    }

    # Create folders if they don't exist
    for folder in file_types.keys():
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Move files to corresponding folders
    for file in os.listdir():
        for folder, extensions in file_types.items():
            if file.endswith(tuple(extensions)):
                shutil.move(file, os.path.join(folder, file))
                print(f'Moved: {file} to {folder}/')

if __name__ == "__main__":
    directory = input("Enter the directory to organize: ")
    organize_files(directory)


import pandas as pd

def clean_data(file_path):
    # Load the data
    df = pd.read_csv(file_path)

    # Remove rows with missing values
    df.dropna(inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Save the cleaned data to a new CSV file
    cleaned_file_path = 'cleaned_' + file_path
    df.to_csv(cleaned_file_path, index=False)
    print(f'Cleaned data saved to {cleaned_file_path}')

if __name__ == "__main__":
    file_path = input("Enter the path to the CSV file to clean: ")
    clean_data(file_path)



import os
import shutil

def clear_temp_files():
    temp_dir = os.environ.get('TEMP')
    if temp_dir:
        print(f'Clearing temporary files from: {temp_dir}')
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f'Deleted file: {file_path}')
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f'Deleted directory: {file_path}')
            except Exception as e:
                print(f'Error deleting {file_path}: {e}')
    else:
        print('No temporary directory found.')

if __name__ == "__main__":
    clear_temp_files()