# Package
- Contained in a directory dedicated to hosting your files.
- It requires a __init__.py as identifier. In principle, with it being empty it is enough.
- You can have as many Python files as you need.
- It can contain sub packages.

# Sub Package
- Sub-packages are created in the same way and are contained in the parent package folder.

# Example:
_See myPackage/AgusPackage_

```py
from AgusPackage import sum_subs
from AgusPackage.subPackage import hello

sum_subs.mySum(1, 2)
sum_subs.mySub(1, 2)
hello.say_hello()
```