#!/usr/bin/env python3

# Created by Joanne Santhosh
# Created on: Dec 2022
# This program finds the even numbers in a list


def even_numbers(list_U):
    list2 = []
    loop_counter = 0

    for single_element in list_U:
        if loop_counter % 2 == 0:
            list2.append(single_element)
        loop_counter += 1

    return list2


def main():
   # This function takes the input and produces a list

    list_U = []

    # input
    for loop_counter in range(0, 10):
        single_random_number = random.randint(0, 100)
        random_numbers.append(single_random_number)

    list2 = odd_indices(list_U)

    print("")
    print(list_U)
    print("The elements in odd positions in the list are: {0}".format(list2))


if __name__ == "__main__":
    main()
