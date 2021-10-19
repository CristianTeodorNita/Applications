'''
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) both recursive and iterative.
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
'''

def iterative_sum_of_positive(number):
    sum_of_positive = 0
    while number > 0:
        sum_of_positive += number
        number -= 2
    return sum_of_positive


print("Calling iterative methods:")
print(iterative_sum_of_positive(6))
print(iterative_sum_of_positive(10))
# 9 + 7 + 5 + 3 + 1
print(iterative_sum_of_positive(9))


def recursive_sum_of_positive(number):
    if number < 1:
        return 0
    else:
        return number + recursive_sum_of_positive(number - 2)


print("Calling recursive methods:")
print(recursive_sum_of_positive(6))
print(recursive_sum_of_positive(10))
print(recursive_sum_of_positive(9))
