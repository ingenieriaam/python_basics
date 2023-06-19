####################################################
# Pathlib module (for any OS)

from pathlib import Path
folder = Path('C:/Users/aortiz/Documents/python/python_basics/day6/test.txt')
# not required open or close


if not folder.exists():
    print("Folder does not exist")
else:
    print("Folder exists")
    print(folder.read_text())
    print(folder.name)
    print(folder.suffix)
    print(folder.stem)

from pathlib import PureWindowsPath
folder = Path('C:/Users/aortiz/Documents/python/python_basics/day6/test.txt')
folder_win = PureWindowsPath(folder)
print(folder_win)

####################################################
# Path objects

base = Path.home()
guide = Path('Barcelona','SagradaFamilia.txt')
print(base)
print(guide)
guide = Path(base,'Barcelona','SagradaFamilia.txt')
print(guide)
print('=======================================')

guide2 = guide.with_name('La_pedrera.txt')
print(guide2)
print('=======================================')

print(guide.parent)
print(guide.parent.parent)
print('=======================================')

guide = Path(Path.home(),'Europa')
for txt in Path(guide).glob('**/*.txt'):
    print(txt)

print('=======================================')

guide = Path('Europa','España','Barcelona','Sagrada Familia.txt')
in_europe = guide.relative_to(Path('Europa'))
in_spain = guide.relative_to(Path('Europa','España'))
print(in_europe)
print(in_spain)

