# Date: 26-09-2019
# Developer: WenLong Wu
# Python programming practice

# Sentence Capitalizer

# This program accepts a string as an argument and returns a copy of the
# string with the first character of each sentence capitalized.

def sentence_cap(the_sentence):

    new_sentence = the_sentence.split('.')

    for n in new_sentence:
        print(n.capitalize(), end = '.')


def main():

    sentence = input("Enter the string: ")

    sentence_cap(sentence)

main()
