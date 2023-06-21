#####################################
# Os module

import os
print(os.getcwd()) # Get current working directory
file = open('file.txt', 'w')
file.write('Hello')
file.close()

print(os.listdir()) # List all files in the current directory

import shutil
shutil.move('file.txt', 'new_file.txt') # Move file to a new location

# Removes
# os.unlink('file.txt') # Removes file
# os.rmdir('new_dir') # Removes directory (empty)
# Removes directory (non-empty)
# DANGER!: Use with caution, no asking for confirmation
# and not use the recycle bin
# shutil.rmtree('new_dir') 
#
# Alternative (not native):
# import send2trash
# send2trash.send2trash('file.txt') # Send file to recycle bin

# Walk through a directory
from pathlib import Path
path = Path('C:/Users/aortiz/Documents/python/python_basics/day9')
print(os.walk(path))

path = Path('C:/Users/aortiz/Documents/python/python_basics/day8')
for folder, subf, file in os.walk(path):
    print(f'in {folder}')
    print('the sub folders are:')
    for sub in subf:
        print(f'\t{sub}')
    print('the file are:')
    for file in file:
        print(f'\t{file}')
    print('\n')