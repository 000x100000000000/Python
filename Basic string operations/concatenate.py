# Date: 22-09-2019
# Name: WenLong Wu
# Python programming practice

# Concatenate

# This program concatenates strings.

def main():

    name = 'Carmen'

    print("The name is", name)

    name = name + " Brown"

    print("Now the name is", name)

    print()

    # Name

    full_name = "Patty Lynn Smith"
    print("Full name:", full_name)

    print()

    # string[start : end]

    middle_name = full_name[6:10]
    print("string[6:10]")
    print (middle_name)

    print()
    
    # string[start:]

    last_name = full_name[11:]
    print("string[11:]")
    print(last_name)

    print()

    # string[:end]
    first_name = full_name[:5]
    print("string[:5]")
    print(first_name)

    print()

    # string[:] / string[::]
    my_string = full_name[:]
    print("string[:]")
    print(my_string)

    print()

    # string[0 : len(full_name)]
    my_string = full_name[0:len(full_name)]
    print("string[0:len(full_name)]")
    print(my_string)

    print()

    # string[start:end:jump]
    letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(letter[0:26:2])

    print()

    # string[-5:]
    last_name = full_name[-5:]
    print("string[-5:]")
    print(last_name)

    print()
    
# Call the main function.
main()
