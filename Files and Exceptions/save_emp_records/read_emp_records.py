# Date: 04-09-2019
# Name: WenLong Wu
# Python programming pratice

# Read emp records

# This program displays the records that are
# in the employees.txt file.

def main():

    employees_file = open('employees.txt', 'r')

    name = employees_file.readline()
    
    while name != '':

        id_number = employees_file.readline()
        dept = employees_file.readline()

        name = name.rstrip('\n')
        id_number = id_number.rstrip('\n')
        dept = dept.rstrip('\n')

        print("Name:", name)
        print("ID:", id_number)
        print("Dept:", dept)

        print()

        name = employees_file.readline()

    # Close the file.
    employees_file.close()

# Call the main
main()
