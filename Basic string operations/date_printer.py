# Date: 23-09-2019
# Developer: WenLong Wu
# Python programming practice

# Date pinter

# This program reads a string from the user containing a date in
# the form mm/dd/yyyy. It should print the date in the form
# Sep 23,2019.

def main():

    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
             'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


    user_input = input("Enter the date: ")

    date = user_input.split('/')

    print(month[int(date[0]) - 1], end= ' ')

    print(date[1], date[2], sep=',')

main()

    
