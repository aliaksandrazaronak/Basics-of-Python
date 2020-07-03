import os

FILE_PREFIX = "spam"

new_list = []

for file in os.listdir():
    if file.startswith(FILE_PREFIX):
        new_list.append(file)

for index, file in enumerate(new_list, start=1):
    if str(index) not in file:
        file_postfix = str(index).zfill(3)
        new_file = f"{FILE_PREFIX}{file_postfix}.txt"
        os.rename(file, new_file)
print(os.listdir())
