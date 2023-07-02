####################################################
# General use
myDict = {'k1': 'value1', 'k2': 'value2'}
print(myDict)

res = myDict['k1']

client = {'name': 'Juan', 'lastname': 'Fuentes', 'peso': 88}
print(client['name'])

myDict = {'k1': 'value1', 'k2': [1, 2, 3, 4, 'e'], 'k3': client}
print(myDict['k3']['name'])
print(myDict['k2'][4].upper())

new = {1: 'a', 2: 'c'}
new[3] = 'c'
print(new)
new[3] = 'C'
print(new)

print(new.keys())
print(new.values())
print(f'This is a tuple {new.items()}')
