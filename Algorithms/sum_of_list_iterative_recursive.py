'''
2.	Write a Python program of recursion and iterative list sum.
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21
'''

test_data = [1, 2, [3,4], [5,6]]


def iterative_sumOfElements(lista):
    # all_numbers = []
    sum_of_numbers = 0
    for element in lista:
        if type(element) == int:
            # all_numbers.append(element)
            sum_of_numbers += element
        elif type(element) == list:
            for subelement in element:
                # all_numbers.append(subelement)
                sum_of_numbers += subelement
    # for number in all_numbers:
    #     sum_of_numbers += number
    # return sum_of_numbers
    return sum_of_numbers

print(iterative_sumOfElements(test_data))  # in this point the function works as we expected -- can be optimized


def recursive_sumOfElements(lista):
    if len(lista) == 0:
        return 0
    for element in lista:
        if type(element) == int:
            return element + recursive_sumOfElements(lista[1:])
        else:
            lista.extend(element)
            return recursive_sumOfElements(lista[1:])


def recursive_sumOfElements1(lista):
    sum_of_numbers = 0
    if len(lista) == 0:
        return 0
    for element in lista:
        if type(element) == int:
            sum_of_numbers += element
        else:
            sum_of_numbers += recursive_sumOfElements1(element)
    return sum_of_numbers

print(recursive_sumOfElements(test_data))  # same at this point is working -- still can be optimized
print(recursive_sumOfElements1(test_data))  # same at this point is working -- still can be optimized
