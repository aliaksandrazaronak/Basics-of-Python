import os

FILE_PREFIX = "spam"

new_list = []

for file in os.listdir():
    if file.startswith(FILE_PREFIX):
        new_list.append(file)

for index, file in enumerate(new_list, start=1):
    if file.find(str(index)) == -1:
        new_file = FILE_PREFIX + "00" + str(index) + ".txt"
        os.rename(file, new_file)
print(os.listdir())
