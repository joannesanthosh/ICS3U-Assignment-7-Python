#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Jan 2023
# This program identifies how many even numbers there are

import random


def find_even_number(list_of_numbers):
    even_number = list_of_numbers[0]

    for counter in range(0, len(list_of_numbers)):
        if list_of_numbers[counter] % 2 == 0:
            even_number += 1

    return even_number


def main():
    # this function generates 10 random numbers

    random_numbers = []

    for loop_counter in range(0, 100):
        single_random_number = random.randint(1, 50)
        random_numbers.append(single_random_number)
        print(
            "The random number {0} is: {1}".format(
                loop_counter + 1, random_numbers[loop_counter]
            )
        )

    # calls function
    even_number = find_even_number(random_numbers)
    print("")
    print("There are {0} even numbers in this list".format(even_number))

    print("\nDone.")


if __name__ == "__main__":
    main()
