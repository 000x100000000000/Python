#### Random number guessing game ####
# This program will generate a random number in range
# 1 through 100, and ask the user to guess what the number is.

import random

# Constants for the program
again = 'y'

# The main funtion
def main():
    # Display the title
    display_title()

    # Game_star
    game_star()

# The display_title shows the instruction for the user.
def display_title():

    print("*** RANDOM NUMBER GUESSING GAME ***")
    print("The system will generate a number 1 - 100 randomly")
    print("If your guess is higher then the ramdom number")
    print("system will display \"Too high, try again.\"")
    print("If your guess is lower then the ramdom number")
    print("system will display \"Too low, try again.\"")

def game_star():

    print("Game stared !!!!!")
    number = random.randint(1, 100)

    answer = int(input("Please enter your answer: "))

    count = 1

    while answer != number:
        
        if answer >= number:
            print("Too high, try again.")
            answer = int(input("Please enter your answer: "))
        elif answer <= number:
            print("Too low, try again.")
            answer = int(input("Please enter your answer: "))
        else:
            print("Error, invalid input.")
            answer = int(input("Please enter your answer: "))

        count += 1

    # Loop ended
    print("Congratulations !!! you guessed", count, "times")
    
# Call the main function
while again == 'y' or again == 'Y':
    main()

    # Run again?
    again = input("Do you want to play again? (y = yes): ")
