# This program displays five random
# numbers in the range of 1 through 100.
import random

def main():
    for cout in range(5):
        number = random.randint(1, 100)
        # Display the number
        print(number)

# Call the main function
main()
