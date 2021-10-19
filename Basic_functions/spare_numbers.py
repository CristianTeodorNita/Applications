'''
Aceasta functie returneaza o lista de numere pare mai mici decat inputul.
'''


def lista_numere_pare_for(numar_final):
    numere_pare = []
    for numar in range(numar_final):
        if numar % 2 == 0:
            numere_pare.append(numar)
        numar += 1
    return numere_pare


def lista_numere_pare_while(numar_final):
    numere_pare = []
    numar = 0

    while numar < numar_final:
        if numar % 2 == 0:
            numere_pare.append(numar)
        numar += 1
    return numere_pare

print(lista_numere_pare_for(int(input("Adaugati numarul limita pentru primul caz: "))))
print(lista_numere_pare_while(int(input("Adaugati numarul limita pentru al doilea caz: "))))
