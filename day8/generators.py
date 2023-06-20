###########################################
# Allows you to get partial results 
# ((helps save memory), so I can generate 
# them as I need them.
# keyword: Yield (produce)

def myFunc():
    return 4

def myGenerator():
    yield 4

print(myFunc())

# hasn't produced the output, because I haven't asked it yet !!!
print(myGenerator())
# to produce it:
gen = myGenerator()
print(next(gen)) # this is an iterator itself

print('====================================')

def myFunc():
    myList = []
    for i in range(1,5):
        myList.append(i*10)
    return myList

def myGenerator():
    for i in range(1,5):
        yield i*10
    # When asked, pick up where you left off

print(myFunc())

# hasn't produced the output, because I haven't asked it yet !!!
print(myGenerator())
# to produce it:
gen = myGenerator()
print(next(gen)) # this is an iterator itself
print(next(gen)) # this is an iterator itself
print(next(gen)) # this is an iterator itself
print(next(gen)) # this is an iterator itself
# This throws an error since it no longer 
# iterates given the function it should do (up to 5)
# print(next(gen)) 
print('====================================')

def myGen():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x

gen = myGen()
print(next(gen)) 
print(next(gen)) 
print("hello world") 
print(next(gen)) 

print('====================================')
def myGen():
    x = 0
    while True:
        x += 1
        yield x
generator = myGen()
print(next(generator)) 