# This program shows how to return
# multiple values.
def main():
    # Get user's name
    first_name, last_name = get_name()

    # Displays user's name
    print("Your name is ", first_name, ' ', last_name, ".", sep='')

# The get_name function ask user user
# to enter their name then returns to main
def get_name():
    # Get the user's first and last names.
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    # Return both name.
    return first, last

# Call the main function
main()
