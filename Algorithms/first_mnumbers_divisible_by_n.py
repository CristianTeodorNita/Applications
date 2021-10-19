'''
Write a program in which:
-  Write a method in which we generate first m numbers divisible by n. In this case, we want to get in a list and print
    the first 500 numbers divisible by 7.

-  save all of those numbers in a file, one number per each row. The file will be called „file_numbers.txt"
In the next steps, we're interested in using as little memory as possible.

-  create a generator which does exactly the same thing as above: generate the first 500 numbers divisible by 7
    (the number of numbers generated is parametrizable) and save it to a file called "file_numbers_new.txt"

-  read the numbers from file ("file_numbers_new.txt") and compute their average without keeping the entire list in memory.
'''

def write_first_divisible_numbers(filename, first_numbers, divisible_by):
    first_divisible_numbers_list = get_first_divisible_numbers(first_numbers, divisible_by)
    write_list_to_file(filename, first_divisible_numbers_list)


def get_first_divisible_numbers(first_numbers, divider):
    my_list = []
    number = 0
    while len(my_list) < first_numbers:
        if is_divisible(number, divider):
            my_list.append(number)
        number += divider
    return my_list

def first_divisible_numbers_generator(first_numbers, divider):
    number = 0
    i = 0
    while i < first_numbers:
        if is_divisible(number, divider):
            yield number
        number += divider
        i += 1


def is_divisible(number, divider):
   return (number % divider) == 0


# print([number for number in first_divisible_numbers_generator(500, 7)])
def write_generator_to_file(filename, first_numbers, divider):
    with open(filename, "w") as f:
        for number in first_divisible_numbers_generator(first_numbers, divider):
            f.write(str(number) + "\n")

def write_list_to_file(filename, my_list):
    with open(filename, "w") as f:
        for element in my_list:
            f.write(str(element) + "\n")

def read_from_file_and_compute_average(filename):
    with open(filename, "r") as f:
        sum_of_numbers = 0
        counter = 0
        for line in f:
            sum_of_numbers += int(line)
            counter += 1
        return sum_of_numbers / counter

print(read_from_file_and_compute_average("file_numbers_new.txt"))

write_first_divisible_numbers("file_numbers.txt", 500, 7)
write_generator_to_file("file_numbers_new.txt", 500, 7)


def get_first_divisible_numbers(first_numbers, divider):
    my_list = []
    number = 0
    while len(my_list) < first_numbers:
        if is_divisible(number, divider):
            my_list.append(number)
        number += divider
    return my_list
