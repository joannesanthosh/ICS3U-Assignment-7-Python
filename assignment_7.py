#!/usr/bin/env python3

# Created by Joanne Santhosh
# Created on: Dec 2022
# This program finds the even numbers in a list


import random


def find_even_numbers(list_of_numbers):
    even_number = list_of_numbers[0]

    for counter in range(0, len(list_of_numbers)):
        if list_of_numbers[counter] % 2 == 0:
            even_number = list_of_numbers[counter]

    return even_number


def main():
    # this function uses an array

    my_numbers = []

    # input
    for loop_counter in range(0, 100):
        random_number = random.randint(1, 50)
        my_numbers.append(random_number)
    print("")

    print("Here are 100 random numbers:")

    for loop_counter in range(0, 100):
        print("The random number is: {0}".format(my_numbers[loop_counter]))

# calls function
    even_number = find_even_numbers(random_number)
    print("")
    print("The even numbers are {0}".format(even_number))

    print("\nDone.")


if __name__ == "__main__":
    main()
