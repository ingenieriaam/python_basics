####################################################
# Create functions

def say_hello(name):
    '''
    Function to say hello
    This is a comment
    '''
    print('Hello '+name)

say_hello('Agus')
say_hello('Magui')

def multiply(n1,n2): 
    res = n1*n2   
    return res

print(multiply(2,3))
res = multiply(2,3)
print(res)

####################################################
# Dynamic functions

def check_3_figures(num):
    return num in range(100,1000)

res=check_3_figures(123)
print(res)

def check_3_figures(num_list):
    three_figures_list = []
    for num in num_list:
        if num in range(100,1000):
            three_figures_list.append(num)
        else: pass
    return three_figures_list

res=check_3_figures([123,34,345,46,567,678])
print(res)

price_coffee = [('latte', 2.50), ('espresso', 1.50), ('cappuccino', 2.00)]
def more_expensive_coffee(price_coffee):
    mayor_price = 0
    more_expensive_coffee=''
    for coffee, price in price_coffee:
        if price > mayor_price:
            mayor_price = price
            more_expensive_coffee = coffee
    return more_expensive_coffee, price

coffe, price=more_expensive_coffee(price_coffee)
print(f'The most expensive coffee is {coffe} and it costs {price}')