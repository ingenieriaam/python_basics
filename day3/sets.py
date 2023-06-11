####################################################
# General use
# Do not allow repeated elements
# are immutable
# are not indexed
# does not support mutable objects

mySet = set([1, 2, 3, 4]) # only 1 arg, in this case, a list
print(type(mySet))
print(mySet)

anotheSet = {1,2,3,4}
print(type(anotheSet))
print(anotheSet)

anotheOneSet = {1,1,2,4,5,3,2,1,3,6,7,6,8,8,9,0,0,0,0,0,0,0}
print(anotheOneSet)

print(len(anotheOneSet))
print(2 in anotheOneSet)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)
s1.add(1)
print(s1)

s1.discard(4)
print(s1)
s1.discard(8)
print(s1)

s1.pop() # delete randomly
print(s1)

s1.clear()
print(s1)
