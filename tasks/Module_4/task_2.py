import os

FILE_PREFIX = "spam"

new_list = []

for file in os.listdir():
    if file.startswith(FILE_PREFIX) and os.path.isfile(file):
        new_list.append(file)
        sorted_list = sorted(new_list)

for index, file in enumerate(sorted_list, start=1):
    file_postfix = str(index).zfill(3)
    new_file = f"{FILE_PREFIX}{file_postfix}.txt"
    os.rename(file, new_file)
print(os.listdir())
