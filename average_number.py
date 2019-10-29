#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program shows the the average

import math


def main():

    while True:
        # input
        first_number = input("Input a number(0-100): ")
        second_number = input("Input another number(0-100): ")
        third_number = input("Input a third number(0-100): ")

        # process
        try:
            first_number_as_number = int(first_number)
            second_number_as_number = int(second_number)
            third_number_as_number = int(third_number)
            if first_number_as_number <= 100 and \
                second_number_as_number <= 100 \
                    and third_number_as_number <= 100:
                total_number = (first_number_as_number +
                                second_number_as_number
                                + third_number_as_number) / 3
                # output
                print("The average is {0}".format(total_number))
                break
            else:
                print("Numbers are over 100")
                break
        except(ValueError):
            print("Not valid numbers inputted")
        finally:
            print("")


if __name__ == "__main__":
    main()
