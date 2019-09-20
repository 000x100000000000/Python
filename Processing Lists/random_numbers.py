# Date: 18-09-2019
# Name: WenLong Wu
# Python programming practice

# Random number

# This program assigns random numbers to
# a two-dimensional list.

import random

def main():

    # Create a two-dismensional list.
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    # Fill the list with random numbers.
    for r in range(0, 4):
        for x in range(0, 4):
            values[r][x] = random.randint(1, 100)

    # Display the random numbers.
    print(values)

# Call the main funcion.
main()
