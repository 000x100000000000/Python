# Date: 19-09-2019
# Name: WenLong Wu
# Python programming practice

# Charge account validation

# This program reads the contents of the charge_accounts.txt into a list.
# Also will ask the user to enter a charge account number. The program will
# determine whether the number is valid by searching for it in the list.
# If the number is in the list, the program should display a message indicating
# the number is valid. If the number is not in the list, the program should
# display a message indicating the number is invalid.

def main():

    found = False

    account = int(input("Enter your account number: "))

    account_file = open('charge_accounts.txt', 'r')

    charge_accounts = account_file.readlines()

    for n in charge_accounts:

        if account == int(n.rstrip('\n')):

            found = True

    if found:
        print(account ,"is valid.")

    else:
        print(account, "is invalid.")
        
main()

    
