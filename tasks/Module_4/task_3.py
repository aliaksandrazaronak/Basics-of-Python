import os
import shutil

NEW_FOLDER = "new_test_folder"

for dirpath, dirnames, filenames in os.walk('test_folder'):
    print('Current path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    for file in filenames:
        _, ext = os.path.splitext(file)
        if ext in ('.pdf', '.jpg'):
            os.makedirs(NEW_FOLDER, exist_ok=True)
            file_path = os.path.join(dirpath, file)
            shutil.copy(file_path, NEW_FOLDER)