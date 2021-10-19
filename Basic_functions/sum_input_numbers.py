'''
Aceasta functie calculeaza suma numerelor inputate
'''

def suma_numerelor(*numere):
    rezultat = 0
    for numar in numere:
        rezultat += numar
    return rezultat


print(suma_numerelor(1, 2, 10, 40))
print(suma_numerelor(-1, 2))
