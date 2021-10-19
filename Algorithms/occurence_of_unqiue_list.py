'''
Count the occurrences of each item and display them in a dictionary first by hand, and then using Python functions.
Test Data:  [11, 45, 8, 11, 23, 45, 23, 45, 89]
Expected Result: {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
'''

test_data = [11, 45, 8, 11, 23, 45, 23, 45, 89]

def iterative_occurences(list):
    dict_data = {}
    for element in list:
        if element in dict_data:
            dict_data[element] += 1
        else:
            dict_data[element] = 1
    return dict_data


print(iterative_occurences(test_data))


def iterative_occurences1(my_list):
    return {elem: my_list.count(elem) for elem in set(my_list)}

from collections import Counter


def iterative_occurences2(my_list):
    return dict(Counter(my_list))

print(iterative_occurences2(test_data))
