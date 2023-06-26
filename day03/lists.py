####################################################
# List utilities
myList = ['a', 'b', 'c']
otherList = ['a', 55, [12, True]]
print(myList)
print(otherList)

thirdList= myList+otherList
print(thirdList)

thirdList.append('g')
print(thirdList)
thirdList.pop()
print(thirdList)
popped = thirdList.pop(0)
print(popped)

alphaList = [3,7,1,5,9,2,4,6,8,0]
alphaList.sort()
print(alphaList)
# but alphaList.sort() have not a return value
alphaList.reverse()
print(alphaList)