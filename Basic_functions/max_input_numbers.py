'''
Aceasta functie determina maximul dintre numerele inputate.
'''

def maxim(**numere):
    max = 0
    for nume, valoare in numere.items():
        if valoare > max:
            max = valoare
    return max

print(maxim(numar_1=1, numar_2=10, numar_3=55))