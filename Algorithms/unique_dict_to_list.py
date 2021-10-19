'''
Return a list containing the unique values from a dictionary
Test Data:  {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53,'july':54, 'Aug':44, 'Sept':54}
Expected Result: [47, 52, 44, 53, 54]
'''

test_dict = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53,'july':54, 'Aug':44, 'Sept':54}

def unique_values(my_dict):
    my_set = set(my_dict.values())
    return list(my_set)


def unique_values1(my_dict):
    my_list = []
    for key, value in my_dict.items():
        if value not in my_list:
            my_list.append(value)
    return my_list


print(unique_values(test_dict))
print(unique_values1(test_dict))
