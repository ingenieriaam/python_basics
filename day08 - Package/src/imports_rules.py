#############################################
# Modules search
import sys
# 1. Search in this vupla to be requested (C modules)
print(sys.builtin_module_names)
# 2. Check the routes on this list
print(sys.path)

#############################################
# Another path module
from pathlib import Path
proj_path    = 'python_basics'
day_path     = 'day08 - Package'
module_path  = Path(Path.home(), proj_path, day_path)
sys.path.append(module_path.__str__())
print(sys.path)

#############################################
# Module import
from AgusPackage import new_module as nm
nm.some_function()
nm.some_class()
print(nm.variable)