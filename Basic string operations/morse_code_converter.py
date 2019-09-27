# Date: 23-09-2019
# Developer: Wenlong Wu
# Python programming practice

# Morse code convertor

# This program asks the user to enter a string, and then converts that
# string to Morse code.

def morse_code():

    code = {' ':' ', ',':'--..--', '.':'.-.-.-', '?':'..--..', 0:'-----',
            1:'.----', 2:'..---', 3:'...--', 4:'....-', 5:'.....',
            6:'-....', 7:'--...', 8:'---..', 9:'----.', 'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..',
            'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.',
            'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.-', 'Z':'--..'}

    user_input = input("Enter your message: ")

    for n in user_input.upper():

        if n in code:
            print(code[n], end=' ')

morse_code()
