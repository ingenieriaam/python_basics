####################################################
# Logic comparisons

myBool = 12 < 23 < 34
print(myBool)

myBool =(12 < 23) and (23 < 34)
print(myBool)

myBool =( 12 == 10) or (23 < 34)
print(myBool)

text = 'sentence is here'
myBool = 'sentence' in text
print(myBool)

myBool = 'python' not in text
print(myBool)