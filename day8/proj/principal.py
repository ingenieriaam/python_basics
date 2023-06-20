from numeros import *

op_dic = {
    1: 'Perfumeria',
    2: 'Farmacia',
    3: 'Cosmeticos'
}
op = 0
a = ''

'''
the generators are the ones that 
receive the parameter from the beginning
'''
generators = []
for key,val in op_dic.items():
     generators.append(shiftGen(val))

@welcome_add
def number_take(number):
        return number

while op != 4:
    try:
        op = int(input(f'''
        Seleccione el area que desea:
        1. {op_dic[1]} 
        2. {op_dic[2]} 
        3. {op_dic[3]} 
        4. Salir
        >>> '''))
    except:
        print('\tingrese una opción valida')
        continue
    if op == 4:
        break
    else:
        a = next(generators[op-1])
        number_take(a)
    