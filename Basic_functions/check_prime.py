'''
Aceasta functie determina daca un numar este prim sau nu.
'''


def is_prime(numar):
    result = False
    for x in range(2, numar):
        if (numar % x) == 0:
            break
        else:
            result = True
    return result

print(is_prime(15))
print(is_prime(14))