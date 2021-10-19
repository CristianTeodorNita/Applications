'''
Write a Python program to get the sum of a non-negative integer (there are multiple ways to do that).
Test Data:
sum_digits(345) -> 12
sum_digits(45) -> 9
'''

test_data = 345

def iterative_nonNegSum(number):
    total = 0
    if number > 0:
        string_number = str(number)
        for element in string_number:
            total += int(element)
    return total

def iterative_nonNegSum1(number):
    total = 0
    while number:
        total += number % 10
        # number = number // 10
        # sau
        number //= 10
    return total


print(iterative_nonNegSum(test_data))
print(iterative_nonNegSum(45))
print(iterative_nonNegSum1(test_data))
print(iterative_nonNegSum1(45))

def recursive_nonNegSum(number):
    numbers = str(number)
    if len(numbers) == 1:
        return int(numbers)
    else:
        return int(numbers[0]) + recursive_nonNegSum(int(numbers[1:]))


print(recursive_nonNegSum(test_data))
print(recursive_nonNegSum(45))
