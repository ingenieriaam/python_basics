####################################################
# Range

for i in range(5):
    print(i)

for i in range(1,5):
    print(i)

myList = list(range(1,5))
print(myList)
myList = list(range(3,301,3))
print(myList)

####################################################
# Enumerator

myList = ['a','b','c']
i = 0

for item in myList:
    print(i,item)
    i+=1

for idx,item in enumerate(myList):
    print(idx,item)

myTuple = list(enumerate(myList))
print(myTuple)

####################################################
# Zip 

myList = ['a','b','c']
nums = [1,2,3]

comb = zip(myList,nums)
print(comb)
comb = list(zip(myList,nums))
print(comb)
nums = [1,2,3,4,5]
comb = list(zip(myList,nums))
print(comb)

names = ['john','jane','jill','james','Agus']
ages = [10,20,30,40,50]
cities = ['Kuala lumpur','Cordoba','New York','London','Paris']
comb = list(zip(names,ages,cities))
print(comb)

capital = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
country = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

comb=list(zip(country,capital))

for p,c in comb:
    print(f'The capital of {p} is {c}')

################################################
# Min and Max

myList = [1,2,3,4,5]
print(min(myList))
print(max(myList))

names = ['john','jane','jill','james','Agus']
print(min(names))
print(max(names))


name = 'Charles'
print(min(name))
name = 'charles'
print(min(name))

dic = {'a':45,'b':11,'c':99}
print(min(dic))
print(min(dic.values()))

#################################################
# Randoms
# the name of file can't be same as module
from random import *
print(randint(1,100))

ran = uniform(1,5)
print(ran)

colors = ['red', 'blue', 'yellow']
print(choice(colors))

nums = list(range(5,50,5))
shuffle(nums)
print(nums)

#################################################
# List comprehension

word = 'python'
list1 = []
for letter in word:
    list1.append(letter)
print(list1)

list2 = [letter for letter in word]
print(list2)

list3 = [n/2 for n in range(5,50,5)]
print(list3)

list4 = [n/2 for n in range(5,50) if n%2==0]
list5 = [n if n*2>10 else 'no' for n in range(0,21,2)]
print(list4)
print(list5)

foot = [10,20,30,40,50]
meters = [p/3.2808 for p in foot]
print(meters)