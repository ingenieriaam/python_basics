# Unzip the instructions
import shutil
# shutil.unpack_archive('Proyecto+Dia+9.zip','Finish_unzip', 'zip')

import re
import os
import datetime
import time
from pathlib import Path
import math

###############################################################################
# Initial text

myDay = datetime.date(2019,12,1) # get date object
today = myDay.today()
day = today.day
mouth = today.month
year = today.year
print('----------------------------------------------------')
print(f'Fecha de búsqueda: {day}/{mouth}/{year}\n')
print('ARCHIVO\t\t NRO. SERIE')
print('-------\t\t ----------')

###############################################################################
# Search for serial number
# Serial number format
# - [N] + [three letters] + [-] + [5 numbers]
# e.g.: Nryu-12365
pattern = r'N\w{3}-\d{5}'

path = Path('C:/Users/aortiz/Documents/python/python_basics/day9/proj/Finish_unzip/Mi_Gran_Directorio')

info = {}
init = time.time()
for folder, subf, files in os.walk(path):
    for file in files:
        file_path = os.path.join(folder, file)
        f = open(file_path, 'r')
        for line in f:
            search = re.search(pattern, line)
            if search:
                info[file]=search.group()
                break
        f.close()
final = time.time()

###############################################################################
# Information print
for key, value in info.items():
    print(f'{key}\t\t {value}')

print(f'\nNúmeros encontrados: {len(info)}')
print(f'Duración de la búsqueda: {math.ceil(final-init)} segundos')

print('----------------------------------------------------')
