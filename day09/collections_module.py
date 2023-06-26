#####################################
# Counter
from collections import Counter

numbers = [1, 2, 3, 2, 4, 1, 1, 4, 5]

# Count how many times each number appears
print(Counter(numbers)) # this is a dictionary

print(Counter('Mississippi')) 

sentence = ' Al pan, pan, y al vino, vino'
print(Counter(sentence.split())) 

series = Counter([1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4])
print(series.most_common())
print(series.most_common(1))
print(series.most_common(2))
print(list(series)) # Get individual values without repeating them

#####################################
# Default dict

from collections import defaultdict
myDic = {'one':'green', 'two':'red', 'three':'blue'}
print(myDic['two'])
# print(myDic['four']) # This is a error. The key not exists

my_dic = defaultdict(lambda: 'nothing') # create a default value
my_dic['one'] = 'green'
print(my_dic['two']) # This is a default value
print(my_dic)

#####################################
# Named tuple
from collections import namedtuple

myTuple = (500,18,65)
print(myTuple[1])

Person = namedtuple('Person', ['name','age','height'])
Agus = Person('Agus', 34, 180)
print(Agus.name)
print(Agus.age)
print(Agus.height)

print(Agus[0])
print(Agus[1])
print(Agus[2])

#####################################
# Deque (double ended queue)

from collections import deque

# Create an empty queue
queue = deque()

# Add elements to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.appendleft(0)
queue.appendleft(-1)
queue.appendleft(-2)

# Remove elements from the queue
queue.popleft() # Removes the first element of the queue (-2)
queue.pop() # Removes the last element of the queue (3)

print(queue) # Prints the current queue [2]

city_list = deque()
a=["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
city_list.extend(a) # queue initialize
