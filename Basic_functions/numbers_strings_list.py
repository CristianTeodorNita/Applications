'''
Aceasta functie separa o lista cu elemente de tip string si integers in liste separate
'''


def split_list(lista_originala):
    string_list = [element for element in lista_originala if isinstance(element, str)]
    numbers_list = [element for element in lista_originala if type(element) == int or type(element) == float]
    return [string_list, numbers_list]


gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]
print(split_list(gadgets))