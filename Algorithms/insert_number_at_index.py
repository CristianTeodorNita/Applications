'''
Insert an element in a list at a certain index without using “insert” python function and then using python functions.
Test Data :
insert_element([1, 2, 5, 6, 8, 0], 2, 3) → [1, 2, 3, 5, 6, 8, 0]
'''

initial_list = [1, 2, 5, 6, 8, 0]

def insert_element(my_list, number, index):
    first_list = my_list[:index]
    second_list = my_list[index:]
    first_list.append(number)
    first_list.extend(second_list)
    return first_list

print(insert_element(initial_list, 3, 2))
print(insert_element(initial_list, 3, 0))
print(insert_element(initial_list, 3, 5))
# for index >= len(my_list) slicing will return the full list and so we add our number at the end of the list
print(insert_element(initial_list, 3, 23))
initial_list.insert(0, 77)
initial_list.insert(22, 77)
print(initial_list)
