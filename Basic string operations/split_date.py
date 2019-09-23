# Date: 23-09-2019
# Developer: WenLong Wu
# Python programming practice

# Split date

# This program calls the split method, using the
# '/' character as a separator.

def main():
    # Create a string with a date.
    date_string = '09/23/2019'

    # Split the date.
    date_list = date_string.split('/')

    # Display each piece of the date.
    print("Month:", date_list[0])
    print("Day:", date_list[1])
    print("Year:", date_list[2])

# Call the main function.
main()
