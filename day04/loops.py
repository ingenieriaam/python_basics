####################################################
# for and while loop

myList = ['a','b','c']

for letter in myList:
    letter_number = myList.index(letter)+1
    print(f"the letter is {letter} and the number is {letter_number}")

names = ['john','jane','jill','james','Agus']
for name in names:
    if name.startswith('j'):
        print(name)

numberList = [1,2,3,4,5]
myValue = 0
for num in numberList:
    myValue = myValue + num
print(myValue)

word = 'python'
for i in word:
    print(i)
for i in 'python':
    print(i)

for a,b,c in [[1,2,3],[4,5,6],[7,8,9]]:
    print(a)
    print(b)
    print(c)

dic = {'a':1,'b':2,'c':3}
for key,val in dic.items():
    print(key,val)

####################################################

coins = 5
while coins > 0:
    print(f'I have {coins} coins')
    coins = coins - 1
else:
    print('I have no coins')

response = 's'

while response == 's':
    print('Do you want to continue?')
    response = input()
else:
    print('Thank you')

#---------------------------------------------------
while response == 's':
    pass

name = input('What is your name?')

for letter in name:
    if letter == 't':
        break
    elif letter == 'u':
        continue
    elif letter == 'g':
        pass
    print(letter)

