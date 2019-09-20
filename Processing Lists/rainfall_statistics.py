# Date: 19-09-2019
# Name: WenLong Wu
# Python programming practice

# Rainfall statisics

# This program lets the user enter the total rainfall for each of 12
# months into a list. The program should calculate and display the total
# for the year, the average monthly rainfall, and the months with the
# highest and lowest amounts.

def main():

    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
              'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

    rainfall = []

    total = 0
    
    for x in months:

        print("Enter the rainfall for", x, ': ', end='')

        rainfall_content = float(input())

        rainfall.append(rainfall_content)

        total += rainfall_content

    print("The total:", total)
    print("The average: ", total/len(rainfall))
    print("The highest:", max(rainfall))
    print("The lowest:", min(rainfall))

main()
    
