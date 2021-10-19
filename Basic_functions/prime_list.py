'''
Aceasta functie returneaza o lista cu numerele prime pana la numarul de input.
'''

def lista_numere_prime_1(numar_final):
    numere_prime = []

    for numar in range(2, numar_final):
        for x in range(2, numar):
            if (numar % x) == 0:
                break
        else:
            numere_prime.append(numar)
    return numere_prime


def lista_numere_prime_2(numar_final):
    numere_prime = []

    for numar in range(2, numar_final):
        is_prime = True
        for x in range(2, numar):
            if (numar % x) == 0:
                is_prime = False
                break
        if is_prime:
            numere_prime.append(numar)
    return numere_prime


print(lista_numere_prime_1(int(input("Adaugati numarul limita pentru primul caz: "))))
print(lista_numere_prime_2(int(input("Adaugati numarul limita pentru al doilea caz: "))))
