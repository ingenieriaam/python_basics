####################################################
# immutable
name = "Carina"
# try, but not found
# name[0] = "K"
# but if you can with your methods
name.replace('C', 'K')
print(name)
# but but, in another object !!!
new = name.replace('C', 'K')
print(new)

####################################################
# concatenable
n1 = 'Kari'
n2 = 'na '
print(n1 + n2)
print((n1 + n2)*5)

sentence = """Learn python,
like any other things,
is a good idea."""

print(sentence)

####################################################
# Content and size
print("python" in sentence)
print("ams" in sentence)

print(len(name))