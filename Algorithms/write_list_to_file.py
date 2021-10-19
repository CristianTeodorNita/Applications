
'''
2. Write the elements of a list to a file in the following way: each row will contain one number from the list.
Do this thing both in an iterative and recursive way.
Method calls :
   write_elem_using_recursion(filename, [1, 2, 5, 6, 8, 4, 9, 23])
   write_elem_iterative(filename, [1, 2, 5, 6, 8, 4, 9, 23])
'''

list_of_numbers = [1, 2, 5, 6, 8, 4, 9, 23]

def iterative_write_file(my_list):
    with open("iterative_write.txt", "w") as f:
        for element in my_list:
            f.write(str(element) + "\n")


def recursive_write_file(my_list):
    with open("recursive_write.txt", "a") as f:
        if len(my_list) == 1:
            f.write(str(my_list[0]) + "\n")
        else:
            f.write(str(my_list[0]) + "\n")
            my_list.pop(0)
            return recursive_write_file(my_list)

def write_list_using_recursion(filename: str, my_list: list):
    with open(filename, "a") as f:
        write_list_recursive(my_list, f)

def write_list_recursive(my_list, f):
    if len(my_list) == 1:
        f.write(str(my_list[0]) + "\n")
    else:
        f.write(str(my_list[0]) + "\n")
        my_list.pop(0)
        return write_list_recursive(my_list, f)
iterative_write_file(list_of_numbers)
# recursive_write_file(list_of_numbers)
write_list_using_recursion("recursive_write.txt", list_of_numbers)