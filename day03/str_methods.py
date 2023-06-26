####################################################
# String type methods

text = "This is the text of Agus"
res = text.upper()
print(res)
res = text.lower()
print(res)
res = text.split() # generate a list of string as default
print(res)
res = text.split('t') # generate a list of string as default
print(res)

####################################################
# Join
a = "Learn"
b = "python"
c = "is"
d = "great !!!"
e = " ".join([a,b,c,d])
print(e)
e = "_".join([a,b,c,d])
print(e)

####################################################
# Find.
# same as index, but, if the character is not in the string,
# it returns "-1", it does not report an error.

print(text.find('A'))
print(text.find('w'))

####################################################
# Replace.
print(text.replace('Agus', 'Another guy'))