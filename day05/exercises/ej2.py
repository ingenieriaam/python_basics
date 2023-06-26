####################################################
#

def letter_ret(word):
    s = set()
    for i in word:
        s.add(i)
    l = list(s)
    l.sort()
    return l

print(letter_ret('hello'))
print(letter_ret('dcba'))