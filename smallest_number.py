# !/usr/bin/env python3

# Created by Joshua Yeung
# Created on October 2021
# This program is to calculate the largest of random number

import random


def smallest_number(random_number):
    # this function is to calculate the average of random number
    smallest = 100
    loop_counter = 0

    # process
    for loop_element in random_number:
        loop_counter = loop_counter + 1
        print("The random number {0} is: {1}".format(loop_counter, loop_element))
        if loop_element < smallest:
            smallest = loop_element

    return smallest


def main():
    # this function is to generater a random number
    random_number = []

    # process
    print("starting ...")
    print("")

    for loop_counter in range(0, 10):
        some_variable = random.randint(1, 100)
        random_number.append(some_variable)

    # call function
    smallest_number_2 = smallest_number(random_number)

    print("\nThe smallest number is {}".format(smallest_number_2))

    print("\nDone")


if __name__ == "__main__":
    main()
