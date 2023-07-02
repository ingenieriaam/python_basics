#####################################
# Compressions and decompressions

import zipfile
myZip = zipfile.ZipFile('test.zip', 'w') # create a new zip (empty)
myZip.write('mi_texto_A.txt')
myZip.write('mi_texto_B.txt')
myZip.close() # close the zip files

OpenZip = zipfile.ZipFile('test.zip', 'r') # open the zip file (read)
OpenZip.extract('mi_texto_A.txt') # extract the file
OpenZip.close() # close the zip files

# with shutil
import shutil
from pathlib import Path
origin_folder = Path('/python_basics/day8 - Package')
dest_folder = Path('/python_basics/day9')
dest_file = 'day8Package'
shutil.make_archive(dest_file, 'zip', origin_folder)

shutil.unpack_archive('day8Package.zip','Finish_unzip', 'zip')