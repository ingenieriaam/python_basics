def welcome_add(func):
    def another_func(op):
        """
        Print the turn number and the result of calling `func` with `op`. Then print a message indicating to wait.
        Parameters:
            op (any): The input parameter to `func`.
        """
        print("Su turno es el:")
        print(func(op))
        print('Wait and you will be served')
    return another_func


def shiftGen(area):
    """
    This function is a generator that yields a number based on the area passed as a parameter.
    It takes one parameter:
        - area [str]: a string that represents the area
    
    It yields:
        - p [int]: a number between 1 and 100 if area is 'perfumeria'
        - f [int]: a number between 1 and 100 if area is 'farmacia'
        - c [int]: a number between 1 and 100 if area is 'cosmeticos'
        - 'invalid area' [str]: if area is not in the possible values
    
    Example:
    ```
    gen = shiftGen('perfumeria')
    next(gen) # Output: 1
    next(gen) # Output: 2
    next(gen) # Output: 3
    ```
    """
    p=0; f=0; c=0
    while True:
        if area == 'Perfumeria': 
            p += 1
            p = p%100
            yield f'P-{p}'
        elif area == 'Farmacia':
            f += 1
            f = f%100
            yield f'F-{f}'
        elif area == 'Cosmeticos':
            c += 1
            c = c%100
            yield f'C-{c}'
        else:
            yield 'invalid area'
