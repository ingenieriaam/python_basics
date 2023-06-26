####################################################
# create a initial list
from random import shuffle
sticks = ['-','--','---','----']

# shuffle(sticks)
def shuffle_sticks(sticks):
    shuffle(sticks)
    return sticks

# ask for try
def ask_try():
    intent = ''
    while intent not in ['1','2','3','4']:
        intent = input('Select a number between 1 and 4\n>>>')
    return int(intent)

# Check intents
def check_intent(myList,intent):
    if myList[intent-1] == '-':
        print('you have to clean the car')
    else:
        print('you are safe')

shuffle_sticks = shuffle_sticks(sticks)
selected = ask_try()
check_intent(shuffle_sticks,selected)