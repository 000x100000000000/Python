# Date: 18-09-2019
# Name: WenLong Wu
# Python programming practice

# Total sales

# This program asks the user to enter a store's sales for each day
# of the week. The amounts should be stored in a list. Use a loop
# to calculate the total sales for the week and display the result.

def main():

    week = ['MONDAY', 'TUESDAY', 'WENESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY',
            'SUNDAY']

    total = 0
    
    week_sale = []

    for n in range(0, 7):

        print("Enter the sale for", week[n], ": ", end='')
        day_sale = float(input())

        week_sale.append(day_sale)

    for x in week_sale:

        total += x

    print("The total sales of the week: $", format(total, ',.2f'), sep='')

main()
