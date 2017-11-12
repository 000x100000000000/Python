# This program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.
import Circle
import Rectangle

# Constants for the manu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# The main function
def main():
    # The choice variale controls the loop
    # and holds the user's menu choice.
    choice = 0

    while choice != QUIT_CHOICE:
        # Display the menu
        display_menu()

        # Get the user's choice.
        choice = int(input("Enter your choice: "))

        # Perfrom the selected action.
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print("The area is ", Circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print("The circumference is", \
                  Circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print("The area is", Rectangle.area(width, length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print("The perimeter is", \
                  Rectangle.perimeter(width, length))
        elif choice == QUIT_CHOICE:
            print("Exiting the program...")
        else:
            print("Error: invalid selection.")

# The display_menu function displays a menu.
def display_menu():
    print("\tMENU")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")

# Call the main function
main()
