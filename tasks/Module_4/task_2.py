import os

FILE_PREFIX = "spam"

filenames_to_check = []

for file in os.listdir():
    if file.startswith(FILE_PREFIX) and os.path.isfile(file):
        filenames_to_check.append(file)
        sorted_filenames = sorted(filenames_to_check)

for index, file in enumerate(sorted_filenames, start=1):
    file_postfix = str(index).zfill(3)
    new_file = f"{FILE_PREFIX}{file_postfix}.txt"
    os.rename(file, new_file)
print(os.listdir())
