#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program loops as many times as the user says to

import string


def main():
    # This function loops

    # Input
    input_as_string = str(input("Enter how many times to loop: "))
    loop_counter = 0
    running_total = 0

    # Process and Output
    try:
        input_as_integer = int(input_as_string)
        if input_as_integer > 0:
            while loop_counter < input_as_integer:
                loop_counter = loop_counter + 1
                running_total = loop_counter + running_total
            print("\nThe sum of all positive integers from 1 to {} is {}.".
                  format(input_as_integer, running_total))
        else:
            print("\n{} is not a positive integer".format(input_as_string))
    except Exception:
        print("\n{} is not a positive integer".format(input_as_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
