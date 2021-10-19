'''
Write a Python program to calculate the value of 'a' to the power 'b' recursive and iterative.
Test Data :
(power(3,4) -> 81
a^0 = 1
1^a = 1
0^a = 0
Example: 3^4 = 3 * 3 * 3 * 3
Note: Find 2 or more possibilities to do this
'''

def iterative_power(a, b):
    total = 1
    i = 0
    while i < b:
        total *= a
        i += 1
    return total


def iterative_power1(a, b):
    total = 1
    for i in range(b):
        total *= a
    return total


def recursive_power(a, b):
    if b == 0:
        return 1
    return a * recursive_power(a, b-1)


test_list = [(3, 4), (3, 0), (1, 4), (0, 4)]

for item1, item2 in test_list:
    print(f"iterative_power({item1}, {item2}): {iterative_power(item1, item2)}")
    print(f"iterative_power1({item1}, {item2}): {iterative_power1(item1, item2)}")
    print(f"recursive_power({item1}, {item2}): {recursive_power(item1, item2)}")
    print(f"{item1}^{item2} = {item1 ** item2}")
    print(f"Function Power {item1}^{item2} = {pow(item1, item2)}")
