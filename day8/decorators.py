#####################################
# Methodology so far:

def mayus_hi(text):
    print('Hi\n')
    print(text.upper())
    print('Bye!!!')
def mayus_only(text):
    print(text.upper())

def lower_only(text):
    print(text.lower())
 
# mayus_hi and mayus only are very same functions
# This is duplicated code
print('====================================')

#####################################
# Methodology with decorators
# The functions are objects too !!!

myFunc = mayus_only
myFunc('PyThOn') # assing a function to a variable

def a_function(func):
    return func

a_function(mayus_hi('PyThOn')) # the function is a argument

def change_text(the_type):
    def mayus_only(text):
        print(text.upper())
    def lower_only(text):
        print(text.lower())

    if the_type == 'may':
        return mayus_only
    elif the_type == 'min':
        return lower_only

operation = change_text('may') # get a function as object
operation('PyThOn')
print('====================================')

# Decorators !!!
def decorator_hi(func):
    """
    This is a decorator that will be applied to any function
    the words "Hi" and "Bye" will be printed before and after 
    the function is called"""
    def another_func(word):
        print('Hi')
        func(word)
        print('Bye')
    return another_func

@decorator_hi
def mayus_only(text):
    print(text.upper())

@decorator_hi   
def lower_only(text):
    print(text.lower())

mayus_only('PyThOn')
lower_only('PyThOn')


# Using like a switsh
def mayus_only(text):
    print(text.upper())
   
def lower_only(text):
    print(text.lower())

mayus_dec = decorator_hi(mayus_only)
lower_dec = decorator_hi(lower_only)

mayus_dec('PyThOn')
lower_dec('PyThOn')
mayus_only('PyThOn')
lower_only('PyThOn')