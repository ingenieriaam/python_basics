####################################################
# General use
# immutable
# They take up less memory

myTuple = (1, 2, 3, 1)
print(type(tuple))

mySecTuple = 1, 2, 3, 'four'

print(mySecTuple[-1])

myTuple = (1, 2, (3, 3.1, 3.14), 4)
print(myTuple[2][2])

t = (1, 2, 3, 4)

s1, s2, s3, s4 = t
print(s1+s2+s3+s4)

print(myTuple.count(1))
print(myTuple.index(1))

myTuple[0] = 4
