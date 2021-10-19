# region First problem
'''
Write a Python program (recursive and iterative) to calculate the sum of a list of numbers by hand and using Python functions.
Test Data: [1, 5, 9, 16]
Expected Result: 31
'''

'''
A. Natural language:
1. Task formulation: program will calculate the sum of a list of numbers
2. The INPUT will be a list of numbers
3. The OUTPUT will be a number that is equal to the sum of the list
4. We will be using python language and will create a function called listSum in a iterative then recursive way.
5. We will check the program/functionality first by running and see if we encounter any error. Then we will test it using the Test Data and Expected Result.
6. We will check on what new situation can appear by testing more scenarios and trying to create a solution for other 
errors that can be encountered and also try to optimize the code (to use less memory and run as fast as possible).
'''

'''
Pseudocode:
READ list_of_numbers
SET total_of_numbers to zero
WHILE number_index < number of elements in list
    BUMP total_of_numbers with number value
ENDWHILE
PRINT total_of_numbers
'''

test_of_data = [1, 5, 9, 16]

def iterative_sumOfList(list):
    sum_of_numbers = 0
    for number in list:
        sum_of_numbers += number
    return sum_of_numbers

def iterative_sumOfList1(lista):
    sum_of_numbers = 0
    i = 0
    length_of_list = len(lista)
    while i < length_of_list:
        sum_of_numbers += lista[i]
        i += 1
    return sum_of_numbers

def iterative_sumOfList2(lista):
    sum_of_numbers = 0
    length_of_list = len(lista)
    for i in range(length_of_list):
        sum_of_numbers += lista[i]
    return sum_of_numbers

print(iterative_sumOfList(test_of_data))  # in this point the function works as we expected -- can be optimized
print(iterative_sumOfList1(test_of_data))  # in this point the function works as we expected -- can be optimized
print(iterative_sumOfList2(test_of_data))  # in this point the function works as we expected -- can be optimized

def recursive_sumOfList(lista):
    if len(lista) == 0:
        return 0
    else:
         return lista[0] + recursive_sumOfList(lista[1:])

print(recursive_sumOfList(test_of_data))  # same at this point is working -- still can be optimized

# endregion