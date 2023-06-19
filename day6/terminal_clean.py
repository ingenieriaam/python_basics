####################################################
# 
from os import system

name = input("What is your name? \n>>>")
age = int(input("How old are you? \n>>>"))

system(f"cls")

print(f"Hello {name}!")
print(f"You are {age} years old!")

