# Date: 26-09-2019
# Developer: WenLong Wu
# Python programming practice

# Alphabetic telephone number translator

# This program will asks the user to enter a 10-character telephone number
# in the format xxx-xxx-xxxx. The application will display the telephone
# number with any alphabetic characters that appeared in the original
# translated to their numeric equivalent.

def phone_code(code):

    phone_alph = code.strip('-')

    phone_number = ''

    for n in phone_alph:
        if n == 'A' or n == 'B' or n == 'C':
            phone_number += '2'
        if n == 'D' or n == 'E' or n == 'F':
            phone_number += '3'
        if n == 'G' or n == 'H' or n == 'I':
            phone_number += '4'
        if n == 'J' or n == 'K' or n == 'L':
            phone_number += '5'
        if n == 'M' or n == 'N' or n == 'O':
            phone_number += '6'
        if n == 'P' or n == 'Q' or n == 'R' or n == 'S':
            phone_number += '7'
        if n == 'T' or n == 'U' or n == 'V':
            phone_number += '8'
        if n == 'W' or n == 'X' or n == 'Y' or n == 'Z':
            phone_number += '9'

    print(phone_alph[:3] + '-' + phone_number[:3] + '-' + phone_number[3:])


def main():

    phone = input("Enter the phone number: ")

    phone_code(phone)

main()
