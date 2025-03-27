#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: March 27, 2025
# This program casts a string to an integer
# then generates a random number between 0 and 9
# and asks the user to guess it

import random


def main():
    # generate random number between 0 to 9
    gen_num = random.randint(0, 9)

    # get the user's number
    user_num_string = input("Enter your number: ")

    # Converts the string into an integer
    try:
        user_num_integer = int(user_num_string)
        if user_num_integer == gen_num:  # Guessing random number game starts here
            print("You guessed correctly")
        else:
            print("Wrong guess, correct number was {}".format(gen_num))
    except Exception:
        print("{} is not a real number.".format(user_num_string))


if __name__ == "__main__":
    main()
