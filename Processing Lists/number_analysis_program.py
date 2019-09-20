# Date: 19-09-2019
# Name: WenLong Wu
# Python programming practice

# Number analysis program

# This program asks the user to enter a series of 20 numbers. Then store
# the numbers in a list and then display the lowest, highest, total and
# average numbers in the list.

def main():

    numbers = []

    total = 0

    for n in range(1, 20+1):

        print("Enter the", n, "number: ", end='')

        numbers_content = float(input())

        numbers.append(numbers_content)

        total += numbers_content

    print("The lowest:", min(numbers))
    print("The highest:", max(numbers))
    print("The total:", total)
    print("The average:", format(total/len(numbers), '.2f'))

main()
