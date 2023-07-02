####################################################
# auto casting
num1 = 20
num2 = 30.5
print(num1+num2)
print(type(num1+num2))

####################################################
# explicit casting
num2 = int(num1)
print(num1)
print(type(num1))

age = int(input("how old are you: "))
print(type(age))
new_age = 1 + age
print("you are going to be "+str(new_age)+" years old")

####################################################
# String formats
x = 10
y = 5
print("my numbers are {} and {}".format(x, y))
print(f"my numbers are {x} and {y}")

colour = "red"
num=234
print(f"The car is {colour} and it's number is {num}")