# This program usess a loop to displayy a
# table of number and their squares.

# Get the starting value.
print("This program displays a list of numbers")
print("and their squares.")
start = int(input("Enter the starting number: "))

# Get the ending limit.
end = int(input("How hign should i go? "))

# Print the table headings.
print()
print("Number\tSquare")
print("--------------")

# Print the numbers and their squares.
for number in range(start, end + 1):
    square = number**2
    print(number, "\t", square)
