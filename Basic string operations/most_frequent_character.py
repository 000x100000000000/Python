# Date: 26-09-2019
# Developer: WenLong Wu
# Python programming practice

# Most frequent character

# This program lets the user enter a string and displays the character
# that appears most frequently in the string.

def count_char(the_sentence):

    word_keeper = ''

    old_count = 0

    word_count = len(the_sentence)

    for n in range(word_count):

        new_count = 0

        for x in range(word_count):

            if the_sentence[n] == the_sentence[x]:

                new_count += 1

            if new_count > old_count:

                word_keeper = the_sentence[n]

                old_count = new_count

    print('Used the most is:' , '\'' + word_keeper + '\'')
    print(old_count, 'times.')

sentence = input("Enter the sentence: ")

count_char(sentence)

        
