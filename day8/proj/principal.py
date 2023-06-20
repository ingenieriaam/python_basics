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
genPerfumeria = shiftGen('Perfumeria')
genFarmacia   = shiftGen('Farmacia')
genCosmeticos = shiftGen('Cosmeticos')
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
    if op == 1:
        a = next(genPerfumeria)
        number_take(a)
    elif op == 2:
        a = next(genFarmacia)
        number_take(a)
    elif op == 3:
        a = next(genCosmeticos)
        number_take(a)
    else:
        print('Nos vemos')
        break