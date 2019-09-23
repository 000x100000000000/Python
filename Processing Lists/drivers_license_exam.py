# Date: 20-09-2019
# Name: WenLong Wu
# Python programming practice

# Drivers license exam

# This program is for driver's license exam. The exam has 20 multiple-choice
# questions. The program will store the correct answers in a list and reads
# the student's answers for each of the 20 questions from a text file and store
# the answers in another list. The student must correctly answer 15 of 20
# questions to pass the exam.

def main():

    count_correct = 0

    count_incorrect = 0

    correct_answer = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                      'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

    user_answer = []

    for n in range(1, 20+1):

        print("Enter your answer for Q", n, ": ", sep='' ,end='')

        user_answer.append(input())

    for x in range(20):

        if user_answer[x] == correct_answer[x]:

            count_correct += 1

        else:

            count_incorrect += 1

    print()
    
    if count_correct >= 15:

        print("You passed!")
        print("Correct:", count_correct)
        print("Incorrect:", count_incorrect)

    else:

        print("You failed!")
        print("Correct:", count_correct)
        print("Incorrect:", count_incorrect)

main()
