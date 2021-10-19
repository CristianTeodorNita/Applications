'''
Write a function to compute the sum of the even and sum of uneven values from a list.
Generate the list randomly with the size 50, elements between 0, 10.
'''
import random
# ca sa poti avea mereu aceeasi lista random ii poti atribui un numar de seed. De fiecare data cand acesta va fi chemat
# se va genera aceasi lista random
random.seed(15)

random_list = [random.randint(0, 10) for x in range(50)]


def sum_of_random(my_list):
    even_total = 0
    uneven_total = 0
    for element in my_list:
        if element % 2 == 0:
            even_total += element
        else:
            uneven_total += element
    return even_total, uneven_total


sum_of_even, sum_of_uneven = sum_of_random(random_list)
print(f"Function will return a set: {sum_of_random(random_list)}")
print(f"Sum of even numbers from list is: {sum_of_even}")
print(f"Sum of uneven numbers from list is: {sum_of_uneven}")
print(f"Function works? {sum_of_even + sum_of_uneven == sum(random_list)}")
even_sum = sum(list(filter(lambda x: (x % 2 == 0), random_list)))
uneven_sum = sum(list(filter(lambda x: (x % 2 != 0), random_list)))
print(f"Lambda generated even sum: {even_sum})")
print(f"Lambda generated uneven sum: {uneven_sum})")