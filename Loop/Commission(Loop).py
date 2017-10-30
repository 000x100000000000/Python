# This program calculates sales commissions.

# Create a variaables to control the loop.
keep_going = 'y'

# Claculates a series of commussions.
while (keep_going == 'y'):
    #Get a salesperson's sales and commission rate.
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))

    # Calculate the commission.
    commission = sales * comm_rate

    # Display the commission.
    print("The commission is $", \
          format(commission, ',.2f'), sep='')

    # See if the user wants to do another one.
    keep_going = input("Do you want to calculate another" + \
                       "commission (Enter y for yes): ")
