# Date: 04-09-2019
# Name: WenLong Wu
# Python programming pratice

# Read coffee records

# This program displays the records in the
# coffee.txt file.

def main():

    coffee_file = open('coffee.txt', 'r')

    name = coffee_file.readline()

    while name != '':

        quantity = coffee_file.readline()

        name = name.rstrip('\n')
        quantity = quantity.rstrip('\n')

        print("Description:", name)
        print("Quantity:", float(quantity))

        name = coffee_file.readline()

    # Close the file
    coffee_file.close()

# Call the main function
main()
