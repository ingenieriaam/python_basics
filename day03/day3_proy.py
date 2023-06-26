####################################################
# Ask the user to enter a text.
# Ask to enter 3 letters
# will return:
# 1. How many times each letter appears in the text (upper and lower case).
# 2. Count words of the text.
# 3. Inform first and last letter
# 4. Inversion of words
# 5. Does python appear in the text?

#################### inputs ######################
text = input("please, enter some text to analyse:\n>>>")
letters = input("please, enter 3 different letters separated by commas:\n>>>")

## 1. How many times each letter appears in the text (upper and lower case).
letters = letters.lower()
l1, l2, l3 = letters.split(',')
text = text.lower()
l1cnt = text.count(l1)
l2cnt = text.count(l2)
l3cnt = text.count(l3)
print(f'{l1} appears {l1cnt} times in the text')
print(f'{l2} appears {l2cnt} times in the text')
print(f'{l3} appears {l3cnt} times in the text')

## 2. Count words of the text.
wordList = text.split()
print(f'The text have {len(wordList)} words')

## 3. Inform first and last letter
print(f'First letter are {text[0]} and last letter are {text[-1]}')

## 4. Inversion of words
wordList.reverse()
print(f'The reversed text is: {wordList}')

## 5. Does python appear in the text?
dictAnswer = {0: 'does not appear', 1: 'appears'}
print(f"The word python {dictAnswer['python' in text]} in the text")