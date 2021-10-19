def is_number(x):
    '''
        Takes a word and checks if Number (Integer or Float).
    '''
    try:
        # only integers and float converts safely
        num = float(x)
        return True
    except ValueError as e:  # not convertable to float
        return False


while True:
    primul_numar = input("Introduceti primul numar: ")
    al_doilea_numar = input("Introduceti al doilea numar: ")
    if is_number(primul_numar) and is_number(al_doilea_numar):
        media_aritmetica = (int(primul_numar) + int(al_doilea_numar)) / 2
        print(f"Media aritmetica a celor doua numere este: {media_aritmetica}")
        break
    print('''
    Informatie neinteleasa,
    Va rog sa folositi  decat numere reale.
    ''')
