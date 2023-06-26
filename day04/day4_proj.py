####################################################
# Ask the user for their name
# They have 8 attempts to guess a number between 1 and 100
# Inform them if the number is incorrect, lower, higher, or correct
# Report how many attempts they have left

####################################################

from random import randint
number = randint(1,101)
attempts = 8
name = input('What is your name?\n>>>')
print(f'Hello {name}, i think a number between 1 and 100 is {number}. Can you guess it?')
while attempts > 0:     
    guess = int(input('Guess a number between 1 and 100:\n>>>'))
    if guess > number:
        print('Lower')
    elif guess < number:
        print('Higher')
    else:
        print(f'Correct {name}!!!')
        break
    attempts = attempts - 1
    print(f'You have {attempts} attempts left')
else: 
    print(f'Sorry {name}, you have no more attempts. The secret number was {number}')
