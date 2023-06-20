#############################################
# Error Handling
def mySum():
    a= int(input("Enter a number: \n>"))
    b= int(input("Enter a number: \n>"))
    print(f'Sum of {a} and {b} is {a+b}')

try:
    # Code that may raise an error
    mySum()
except:
    # Handle the error
    print("Something went wrong")
else:
    # Code that runs if no error
    print("No error")
finally:
    # Code that runs no matter what
    print("I always runs")

print('====================================')

# More specific error handling
try :
    # Code that may raise an error
    mySum()
except ValueError:
    # Handle the error
    print("This is not a number")
except TypeError:
    # Handle the error
    print("You try to concatenate some type (not a number) and a number")
else:
    # Code that runs if no error
    print("No error")
finally:
    # Code that runs no matter what
    print("I always runs")
print('====================================')
###########################################
def ask_for_number():
    while True:
        try:
            num = int(input("Enter a number: \n>"))
        except:
            print("You entered a value that is not a number")
            num=-1
        else:
            print(f"You entered a number {num}")
            break
        finally:
            print("thank you")
    return num

ask_for_number()
