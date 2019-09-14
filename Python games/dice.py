# Date: 26-08-2019
# Name: WenLong Wu
# Python programming pratice

# Dices

import random

MIN = 1
MAX = 6

def main():

    # Create a variable to control the loop.
    again = 'y'

    # Simulate rolling the dice.
    while again == 'y' or again == 'Y':
        print("Rolling the dice ...")
        print("Their values are:")
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        again = input("Roll them again? (y = yes): ")

# Calling the main function
main()
