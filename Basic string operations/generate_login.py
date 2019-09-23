# Date: 22-09-2019
# Name: WenLong Wu
# Python programming practice

# Generate login

# This program gets the user's first name, last name, and
# student ID number. Using this data it generates a
# system login name.

import login

def main():
    # Get the user's first name, last name, and ID number.
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    idnumber = input("Enter your student ID number: ")

    # Get the login name.
    print("You system login name is:")
    print(login.get_login_name(first, last, idnumber))

# Call the main function.
main()
