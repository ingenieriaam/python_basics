####################################################
# *args and **kargs
# The key is the symbols '' or '*'. While the words 
# are usually 'args' and 'kwargs', they could be called 
# anything as long as the asterisk is used as a prefix.

def sum(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sum(1,2,3,4,5))
print(sum(1,2,3,4,5,6,7,8,9,10))

# for dictionarys

def testing(**kwargs):
    print(type(kwargs))

testing(a=1, b=2, c=3)

def sum(**kwargs):
    total = 0
    for k,v in kwargs.items():
        print(f'{k}: {v}')
        total += v
    return total
print(sum(a=1, b=2, c=3))

def sum(n1,n2,*args,**kwargs):
    print(f'First: {n1}')
    print(f'Second: {n2}')
    for a in args:
        print(f'Args: {a}')
    total = 0
    for k,v in kwargs.items():
        print(f'{k}: {v}')
        total += v
    return total


kwargs={'x':6,'y':7,'z':8}
args=(3,4,5)
print(sum(1,2,args,**kwargs))