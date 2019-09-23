# Date: 23-09-2019
# Developer: WenLong Wu
# Python programming practice

# Initials

# This program will gets a string containing a person's first,
# middle, and last names, and then display their first, middle,
# and last initials. For example, if the user enters John William
# Smith the program should display J. W. S.

def main():

    first_name = input("Enter first name: ")

    middle_name = input("Enter middle name: ")

    last_name = input("Enter last name: ")

    print(first_name[:1], middle_name[:1], last_name[:1], sep='.')

main()
