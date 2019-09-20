# Date: 18-09-2019
# Name: WenLong Wu
# Python programming practice

# Read number

# This program is to reads numbers from a file into a list.

def main():

    # Open a file for reading.
    infile = open('numberlist.txt', 'r')

    # Read the contents of the file into a list.
    numbers = infile.readlines()

    # Close the file.
    infile.close()

    # Convert each element to an int.
    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])

        index += 1

    # Print the contents of the list.
    print(numbers)

# Call the main function.
main()
