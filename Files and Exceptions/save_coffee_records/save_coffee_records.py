# Date: 04-09-2018
# Name: WenLong Wu
# Python programming pratice

# Save coffee records

# This program adds coffee inventory records to
# the coffee.txt file.

def main():

    print("Enter the following coffee data:")

    again = 'y'

    coffee_file = open('coffee.txt', 'a')

    while again == 'y' or again == 'Y':

        coffee_des = input("Description: ")

        coffee_quan = input("Quantity (in pounds): ")

        print("Do you want to enter another record?")

        coffee_file.write(coffee_des + '\n')
        coffee_file.write(coffee_quan + '\n')

        again = input("Y = yes, anything else = no: ")

    print("Data appended to coffee.txt.")

# Call the main function
main()
