import os
import shutil

NEW_FOLDER = "new_test_folder"

for dirpath, dirnames, filenames in os.walk('test_folder'):
    print('Current path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    for file in filenames:
        if file.find("pdf") != -1 or file.find("jpg") != -1:
            os.makedirs(NEW_FOLDER, exist_ok=True)
            shutil.copy(dirpath + "\\" + file, NEW_FOLDER)
