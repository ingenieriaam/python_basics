#########################################
# Regular expressions module
# d is a number, D es not a number
# w is a word, W is not a word
# s is a space, S is not a space

import re

text = 'If you need help, call 658-598-9977, 24 hours at your service (see online help)'

pattern = 'help' 
mySearch = re.search(pattern, text)
print(mySearch)
print(mySearch.span())
print(mySearch.start())
print(mySearch.end())

for match in re.finditer(pattern, text):
    print(match.span())

pattern = r'\d{3}-\d{3}-\d{4}' # r means raw string, special characters

mySearch = re.search(pattern, text)
print(mySearch)
print(mySearch.group())

pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # r means raw string, special characters

mySearch = re.search(pattern, text)
print(mySearch)
print(mySearch.group(1))
print(mySearch.group(2))
print(mySearch.group(3))

# Pass condition example

password = input('Enter password: ')
pattern = r'\D{1}\w{7}'

check = re.search(pattern, password)
print(check)

# Other examples
text = 'We do not serve Monday afternoons'
search = re.search(r'Monday|Friday', text) # search for Monday or Friday
print(search)
search = re.search(r'..rve', text) # search for 'any any rve'
print(search)

search = re.search(r'^\D', text) # if pattern start is not a digit
print(search)
search = re.search(r'\D$', text) # if pattern end is not a digit
print(search)
search = re.findall(r'[^\s]', text) # exclude all spaces
print(search)
search = re.findall(r'[^\s]+', text) # exclude all spaces, and cut by groups
print('_'.join(search))

# Mail check
import re

def check_email(email):
    # Define the regular expression to search for ".com" followed by any other set of characters at the end of the text
    pattern = r"\.com(\.[\w]+)?$"
    # pattern = r'@\w+\.com' another option

    search1 = re.search(r'@', email)
    search2 = re.search(pattern, email)

    if search1 != None and search2 != None:
        print("Ok")
    else: 
        print("The email address is incorrect")