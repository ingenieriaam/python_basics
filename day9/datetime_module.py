###################################################
# datetime module
import datetime

myHours = datetime.time(17,36) # get current time
print(type(myHours))
print(myHours)

myDay = datetime.date(2019,12,1) # get current date
print(myDay)
print(myDay.today())
print(myDay.ctime()) 

from datetime import datetime
myDate = datetime(2019,12,1,22,10,15,1045)
print(myDate)
myDate = myDate.replace(year=2023, month=6, day=20)
print(myDate)
a = myDate.now()
print(a.minute)
from datetime import date

born = date(1912, 10, 1)
dead = date(2019, 12, 12)

live = dead - born
print(f'lives {live.days} days')

wake_up = datetime(2023,6,20,12,30,15,1045)
to_sleep = datetime(2023,6,19,0,12,4,100)

print(f'The person sleep{wake_up-to_sleep} hours.')
print('====================================')

############################################
# Time measure
import time

def test_for(num):
    myList = []
    for i in range(num):
        myList.append(i)
    return myList

def test_while(num):
    myList = []
    i = 0
    while i < num:
        myList.append(i)
        i += 1
    return myList

num = 10000
init = time.time()
test_for(num)
final = time.time()
print(final-init)
init = time.time()
test_while(num)
final = time.time()
print(final-init)

import timeit
declaration = """
test_for(10)
"""
setup = """
def test_for(num):
    myList = []
    for i in range(num):
        myList.append(i)
    return myList
"""
for_dur = timeit.timeit(declaration, setup, number=1000000)
# this repeats 1000000 times

declaration = """
test_while(10)
"""
setup = """
def test_while(num):
    myList = []
    i = 0
    while i < num:
        myList.append(i)
        i += 1
    return myList
"""
while_dur = timeit.timeit(declaration, setup, number=1000000)

print(f'Loop for: {for_dur}\n Loop while: {while_dur}')