import os
from pathlib import Path
import random
import string
import shutil
def defolder(file_path):
 shutil.rmtree(str(file_path))
def mFolder(folder_path):
    folder_path = Path(folder_path)
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)
def mFile(file_path,content):
   file_path = Path(file_path)
   if not os.path.isfile(file_path):
    with open(file_path, 'w') as f:
     f.write(content)
def count_files(folder_path):
    folder_path = Path(folder_path)
    file_count = 0
    for _, _, files in os.walk(folder_path):
        file_count += len(files)
    return file_count
def random_char(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))
