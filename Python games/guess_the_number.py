# Date: 16-09-2019
# Name: WenLong Wu
# Python programming practice

# Guess the number

# The computer will think of a random number from 1 to 100,
# and ask you to guess it. It will tell you the range, if
# you guess the number within six times then you win.

# Import random function for generate number.
import random

# Main function.
def main():

    # Introduction.
    print("Hello! What is your name?")

    # Get name from the user.
    name = input()

    # Display the input name with welcome message.
    print("Well,", name, ", I am thinking of a number", \
          "between 1 and 100.")

    print("You win if you guessed the number within 6 times.")

    # Set number random range.
    number_max = 100
    number_min = 1

    # Set counter for counting the times the user tried.
    counter = 1

    # Generate a random number.
    number = random.randint(number_min, number_max)

    print("Take a guess.")

    # Get guess input from the user and take it as int type.
    guess = int(input())

    # Check two number match, display range.
    while guess != number:

        if guess < number:

            number_min = guess

            print(number_min, "--------", number_max)

            guess = int(input())

        elif guess > number:

            number_max = guess

            print(number_min, "--------", number_max)

            guess = int(input())

        # Counter + 1 each time the user had tried.
        counter += 1

    # The user wins if counter less then 6 tried.
    if counter <= 6:

        print("You win within", counter, "times.")

    # The user lose when counter more then 6 tried.
    else:

        print("I'm sorry, you tried", counter, "times.")

# Call the main function.
main()
