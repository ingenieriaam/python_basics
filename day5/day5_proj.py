####################################################
# Hangman
# Displays a series of dashes so that the user can select a letter
# knowing the number of letters in the word.
# The user has 6 lives.
# The game ends when the user finds all the letters.
# For this exercise, the instructor provides a program flowchart.

from random import choice

# Create a list of words to choose for the game
game_words = ['python', 'java', 'kotlin', 'javascript','assembler'] 
the_word = choice(game_words)
word_len = len(the_word)
underscores = "_ " * len(the_word)
lives = 6

def letter_input():
    """
    Takes user input and returns a lowercase letter. If the user input is not a letter, prompts the user to input a valid letter.
    
    Parameters:
    None
    
    Returns:
    str: A lowercase letter
    """
    letter = input("Guess a letter:\n>>> ")
    while letter.isalpha() == False:
        letter = input("Guess a letter (numbers and symbols are not worth):\n>>> ")
    return letter.lower()

def show_updated_word(the_word, let, underscores):
    """
    Takes in a word, a letter, and a string of underscores. Replaces each underscore 
    that represents the position of the letter in the word. Returns the updated 
    string with the replaced underscores. 

    Args:
    - the_word (str): The original word.
    - let (str): The letter to be placed in the corresponding position in the 
      underscores string.
    - underscores (str): A string of underscores that represents the positions of the 
      letters in the word.

    Returns:
    - updated (str): The updated string with the replaced underscores.
    """
    word_len = len(the_word)
    uc = list(underscores)
    for i in range(word_len):
        if the_word[i] == let:
            uc[2*i] = let 
    updated = "".join(uc)
    print(updated)
    return updated

def is_complete(updated):
    for i in updated:
        if i == "_":
            return False
    return True

def is_the_word(word):
    if word == the_word:
        return True
    
####################################################
## Game logic
####################################################
incorrect = []
print('Guess the word !!!')
print(f'{underscores} ({word_len} letters)')
while lives >0:
    lives-=1
    let = letter_input()
    if len(let)==1:
        if let in the_word:
            underscores = show_updated_word(the_word, let, underscores)
            if is_complete(underscores): 
                print("You won!")
                break    
            else:
                print(f'you have {lives} lives left')
        else:
            print(f'the letter {let} is not in the word')
            incorrect.append(let)
            print(f'incorrects letters: {incorrect}')
    else:
        if is_the_word(let):
            print("You won!")
            break 
        else:
            word=list(let)
            for letter in word:
                underscores = show_updated_word(the_word, letter, underscores)
                incorrect.append(letter)
            print(f'incorrects letters: {incorrect}')

print("Game over!")

