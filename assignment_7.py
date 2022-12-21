#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Dec 2022
# This program uses a list


def main():
    # this function uses a list

    words = []
    temp_word = None

    # input
    print("Enter 1 word at a time. Enter STOP to end.")

    temp_word = input("Enter a word: ")
    words.append(temp_word)
    while temp_word.upper() != "STOP":
        temp_word = input("Enter a word: ")
        words.append(temp_word)

    words.pop() # remove the "Stop" that was added
    print("")

    print("Here are the words.")
    for counter in range(0, len(words)):
        print(temp_word)


if __name__ == "__main__":
    main()
