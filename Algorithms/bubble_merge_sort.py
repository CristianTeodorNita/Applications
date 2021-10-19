'''
1. Create a car class which has as members:
- brand
- model
- year
a) Implement __str__() method to show its brand, model, and year and print this information to the console
b) Adapt bubble sort and merge sort methods discussed in class to sort a list of car objects by year.
c) Use Python built in method to sort these objects by brand (alphabetically). (tip: use "key" parameter in built in
sorted() method to achieve that )
d) Use sorted() method directly to sort our list of car objects by year without the "key" parameter (tip: implement
methods __eq__ __gt__ and __ls__ in class Car to achieve that)
Example code:
car1 = Car("Alfa Romeo", "33 SportWagon", 1988)
car2 = Car("Chevrolet", "Cruze Hatchback", 2011)
car3 = Car("Corvette", "C6 Couple", 2004)
car4 = Car("Lincoln", "Navigator SUV", 2015)
car5 = Car("Cadillac", "Seville Sedan", 1995)
car_array = [car1, car2, car3, car4, car5]
'''

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        show = "Brand: " + str(self.brand) + ", model: " + str(self.model) + " year: " + str(self.year)
        return show

    def __eq__(self, other):
        return self.year == other.year

    def __gt__(self, other):
        return self.year > other.year

    def __lt__(self, other):
        return self.year < other.year

def print_list(my_list):
    for element in my_list:
        print(element)

def bubble_sort_obj_list(my_list):
    for i in range(len(my_list) - 1):
        for j in range(0, len(my_list)-1):
            if my_list[j].year > my_list[j+1].year:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

def bubble_sort_obj_list_1(my_list, comparison_function):
    for i in range(len(my_list) - 1):
        for j in range(0, len(my_list)-1):
            if comparison_function(my_list[j], my_list[j + 1]):
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]


def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)


def merge(array, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge
    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index: middle + 1]
    right_copy = array[middle + 1: right_index + 1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index].year < right_copy[right_copy_index].year:
            # se poate face cu lambda ca la bubble comparison function
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        # Opposite case
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1
        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index += 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1

from copy import deepcopy

car1 = Car("Alfa Romeo", "33 SportWagon", 1988)
car2 = Car("Chevrolet", "Cruze Hatchback", 2011)
car3 = Car("Corvette", "C6 Couple", 2004)
car4 = Car("Lincoln", "Navigator SUV", 2015)
car5 = Car("Cadillac", "Seville Sedan", 1995)

car_array = [car1, car2, car3, car4, car5]
car_array_bubble = deepcopy(car_array)
car_array_bubble_lambda = deepcopy(car_array)
car_array_merge = deepcopy(car_array)

print("Original list:")
print_list(car_array)

print("---------------------------------------------------")
bubble_sort_obj_list(car_array_bubble)
print_list(car_array_bubble)

print("---------------------------------------------------")
merge_sort(car_array_merge, 0, len(car_array_merge) - 1)
print_list(car_array_merge)

print("Original list:")
print_list(car_array)

print("---------------------------------------------------")
bubble_sort_obj_list_1(car_array_bubble_lambda, lambda x, y: x.year > y.year)
# bubble_sort_obj_list_1(car_array_bubble_lambda, lambda x, y: x.brand < y.brand)
print_list(car_array_bubble_lambda)

print("Original list:")
print_list(car_array)

print("---------------------------------------------------")
car_array_brand_sorted = sorted(car_array, key=lambda x: x.brand)
print_list(car_array_brand_sorted)

print("Original list:")
print_list(car_array)
print("---------------------------------------------------")
car_array_sorted_2 = sorted(car_array)
print_list(car_array_sorted_2)