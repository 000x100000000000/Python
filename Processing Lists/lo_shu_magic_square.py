# Date: 21-09-2019
# Name: WenLong Wu
# Python programming practice

# Lo shu magic square

# The Lo shu magic square is a grid with 3 rows and 3 columns, contains the
# numbers 1 through 9 exactly. The sum of each row, column and each diagonal
# all add up to the same number.
def welcome_message():

    print("How to win: the sum of all rows must = 15")
    print("Fill in 1 - 9, can not reuse.")
    print()

def play_game(lo_shu):
    
    print("_________________")
    print("|    |     |    |")
    print("|", lo_shu[0][0]," | ", lo_shu[0][1]  ," | ", lo_shu[0][2] ,"|")
    print("_________________")
    print("|    |     |    |")
    print("|", lo_shu[1][0]," | ", lo_shu[1][1]  ," | ", lo_shu[1][2] ,"|")
    print("_________________")
    print("|    |     |    |")
    print("|", lo_shu[2][0]," | ", lo_shu[2][1]  ," | ", lo_shu[2][2] ,"|")
    print("_________________")

    # Empty line.
    print()

def check_row(user_row):

    while user_row < 1 or user_row > 3:
        
        print("That row does not excis. Try again.")
        print()
        user_row = int(input("Which row you wanna change(1-3): "))

    return user_row

def check_column(user_column):

    while user_column < 1 or user_column > 3:
        
        print("That column does not excis. Try again.")
        print()
        user_column = int(input("Which column you wanna change(1-3): "))

    return user_column


def check_input(user_input):
    
    while user_input < 1 or user_input > 9:
        
        print("The number must between 1-9. Try again.")
        print()
        user_input = int(input("Enter 1 - 9: "))

    return user_input

def check_excis(lo_shu, user_input):

    for n in range(3):
        
        for y in range(3):
            
            while lo_shu[n][y] == user_input:
                
                print("That number already excis. Try again!")
                print()
                # Safety check for number.
                try:
                    user_input = int(input("Enter 1- 9: "))
                    user_input = check_input(user_input)
                except:
                    print("Invalid input.")

    return user_input

def check_lose(lo_shu):

    zero_count = 0

    for n in range(3):
        for y in range(3):
            if lo_shu[n][y] == 0:
                zero_count += 1

    if zero_count == 0:

        return True

    elif zero_count > 0:

        return False

def check_win(lo_shu):

    row1_total = 0
    row2_total = 0
    row3_total = 0

    for n in range(3):
        
        row1_total += lo_shu[0][n]
        row2_total += lo_shu[1][n]
        row3_total += lo_shu[2][n]

    if row1_total == 15 and row2_total == 15 and row3_total == 15:

        return True

    else:
        
        return False

def main():

    welcome_message()

    win = False

    lo_shu = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    play_game(lo_shu)

    while not win:

        # Safety check for row.
        try:
            user_row = int(input("Which row you wanna change(1-3): "))
            user_row = check_row(user_row)
        except:
            print("Invalid input.")

        # Safety check for column.
        try:
            user_column = int(input("Which column you wanna change(1-3): "))
            user_column = check_column(user_column)
        except:
            print("Invalid input.")

        # Safety check for number.
        try:
            user_input = int(input("Enter 1 - 9: "))
            user_input = check_input(user_input)
        except:
            print("Invalid input.")

        # Pass all input to game table and safety check.
        user_input = check_excis(lo_shu, user_input)
            
                        
        lo_shu[user_row-1][user_column-1] = user_input

        # Display new game table.
        play_game(lo_shu)

        # Lose conditions.
        if check_lose(lo_shu):

            print("You lose.")

            break
            
        # Win conditions.
        if check_win(lo_shu):
                
            print("You win!!!")
                
            win = True

again = 'y'

while again == 'y':

    main()

    again = input("Want to play again?(y/n) ")
