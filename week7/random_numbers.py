import random


def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)
    append_random_numbers(randnums)
    print(randnums)
    append_random_numbers(randnums, quantity=3)
    print(randnums)


def append_random_numbers(numbers_list: list, quantity: int = 1):

    for i in range(quantity):
        quantity_pseudo = round(random.uniform(0, 100), 1)
        numbers_list.append(quantity_pseudo)


main()
