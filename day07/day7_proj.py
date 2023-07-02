from random import randint
class Persona:
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name

class Cliente(Persona):
    def __init__(self,name,last_name):
        super().__init__(name,last_name)
        self.numero_cuenta = randint(100000000000,999999999999)
        self.balance = 0
    def __str__(self):
        return f'Name: {self.name} {self.last_name}, Count: {self.numero_cuenta}, Balance: ${self.balance}'
    def depositar(self,amount):
        if amount > 0:
            self.balance += amount
            print(f'You have ${self.balance}')
        else: 
            print("Invalid amount")
    def retirar(self,amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient funds")
                print(f'You have ${self.balance}')
        else: 
            print("Invalid amount")
def crear_cliente(name,last_name):
    return Cliente(name,last_name)

def inicio(name,last_name):
    cliente = crear_cliente(name,last_name)
    print(cliente)
    return cliente

clients = {}
print("Welcome to the Bank of the Future")
name = input("Name: \n>>>")
last_name = input("Last name: \n>>>")
key = name+' '+last_name
if key not in clients:
    clients[key] = inicio(name,last_name)
op=0
while op != 4:
    op = int(input("1. Create a new client\n2. Deposit\n3. Withdraw\n4. Exit\n"))
    match op:
        case 1:
            name = input("Name: \n>>>")
            last_name = input("Last name: \n>>>")
            key = name+' '+last_name
            clients[key] = inicio(name,last_name)
        case 2:
            amount = int(input("Amount to deposit: \n>>>"))
            clients[key].depositar(amount)

        case 3:
            amount = int(input("Amount to withdraw: \n>>>"))
            clients[key].retirar(amount)

        case 4:
            print("Bye")

