# Date: 04-09-2019
# Name: WenLong Wu
# Python programming pratice

# Save emp records

# This program gets employee data from user and
# saves it as records in the employees.txt file.

def main():

    employees = int(input("How many employee records do you want to create? "))

    employees_file = open('employees.txt', 'w')

    for employees in range(1, employees + 1):

        print("Enter the data for employee #" + str(employees))

        # Employee informations
        name = input("Name: ")
        id_number = input("ID Number: ")
        department = input("Department: ")

        # Writting employee informations
        employees_file.write(name + '\n')
        employees_file.write(id_number + '\n')
        employees_file.write(department + '\n')

        print()

    # Close the file
    print("Employee records written to employees.txt.")

    employees_file.close()

# Call the main function
main()
