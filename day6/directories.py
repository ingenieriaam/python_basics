####################################################
# Work with files out of current directory

import os

# Get current directory
path = os.getcwd()
print(path)

# Change working directory
path = os.chdir('/')
print(path)
myFile = open("README.md")
print(myFile.read())
myFile.close()

# Create a new directory
path = os.makedirs('C:\\Users\\aortiz\\Documents\\python\\python_basics\\day6\\testFolder')

path = 'C:\\Users\\aortiz\\Documents\\python\\python_basics\\day6\\testFolder\\created.txt'
element_dir = os.path.dirname(path)
element_file = os.path.basename(path)
print(element_dir)
print(element_file)
element_dir, element_file = os.path.split(path)
print(element_dir)
print(element_file)

os.rmdir('C:\\Users\\aortiz\\Documents\\python\\python_basics\\day6\\testFolder')

# Open a file with windows style
another_file = 'C:\\Users\\aortiz\\Documents\\python\\python_basics\\day6\\test.txt'
myFile = open(another_file)
print(myFile.read())
myFile.close()

# Open with path module for any OS
from pathlib import Path
folder = Path('C:/Users/aortiz/Documents/python/python_basics/day6')
file = folder/'test.txt'
myFile = open(file)
print(myFile.read())
myFile.close()