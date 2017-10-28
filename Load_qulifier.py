# This program determines whether a bank customer
# qualifies for a loan.

min_salary = 30000.0 # The minimum annual salary
min_year = 2        # The minimum years on the job

# Get the customer's annual salary
salary = float(input("Enter your annual salary:"))

# Get the number of years on the current job
years_on_job = int(input("Enter the number of" +
                         " yeaars employed:"))

# Determine whether the customer qualifies.
if salary >= (min_salary):
    if years_on_job >= (min_year):
        print ("You qualify for the loan.")
    else:
        print ("You must have been employed", \
               "for at least", min_year, \
               "years to qualify.")
else:
    print ("You must earn at least $", \
           format(min_salary, ',.2f'), \
           " per year to qualify.", sep='')
