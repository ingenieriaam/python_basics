####################################################
# Get a sub-strings (slicing)
text = "ABCDEFGHIJKLM"
frag = text[2:5]
print(f'From indices 2 to 5 {frag}')
frag = text[2:]
print(f'From indices 2 to end {frag}')
frag = text[:5]
print(f'From indices 0 to 5 {frag}')
frag = text[2:10:2]
print(f'From indices 2 to 10 going through 2 characters {frag}')
frag = text[::2]
print(f'From indices 0 to end going through 2 characters {frag}')

sentence = "It's great working with computers. They don't argue, they remember everything and they don't drink your beer"
reversed = sentence[-1::-1]
print(reversed)