####################################################
# Index method

my_text = "This is a test"
print(f'In index 9 we ha a character {my_text[9]}')
print(f't is in index {my_text.index("t")}')

init = 5
finish = 10
character = "a"
print(f'Search the character {character} between indexes {init} and {finish}')
print(f'result: {my_text.index(character,init,finish)}')

character = "y"
print(f'Search the character {character} between indexes {init} and {finish} (but it\'s not there)')
try:
    print(f'result: {my_text.index(character,init,finish)}')
except:
    print('letter not found')

frase = "In theory, theory and practice are the same. In practice, they are not."
print(f'First appearance of the word "practice": {frase.index("practice")}')
print(f'Last appearance of the word "practice" (using rindex): {frase.rindex("practice")}')
