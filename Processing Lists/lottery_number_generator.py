# Date: 18-09-2019
# Name: WenLong Wu
# Python programming practice

# Lottery Number Generator

# This program generates a seven-digit lottery number. The program
# should generate seven random numbers, each in the range of 0
# through 9, and assign each number to a list elements. Then uses
# another loop that displays the contents of the list.

import random

def main():

    bingo = []

    for n in range(7):
        bingo.append(random.randrange(0, 10))

    for x in bingo:
        print(x, end='')

main()
