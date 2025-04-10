

import os

file_path = "test/text.txt"

if os.path.exists(file_path):
    directory, name = os.path.split(file_path)
    atime = os.path.getatime(file_path)
    # print(name)
    print(f"{name} ({directory}) - last access file {atime} sec")
else:
    print(f"Файл {file_path} отсутствует")

