####################################################
#


def contar_primos(lim):
    primos = []
    for i in range(2, lim):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primos.append(i)
    return len(primos), primos

l, primos = contar_primos(100)
print(l, primos)