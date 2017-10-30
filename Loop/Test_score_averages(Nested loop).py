# This program averages test scores. It asks the user for the
# number o students and the number of test scores per student.

# Get the number of students.
num_students = int(input("How many students do you have? "))

# Get thee number of test scores per student.
num_test_scores = int(input("How many test scores per student? "))

# Determine each student's average test score.
for student in range(num_students):
    # Initilize aan accumultor for test scores.
    total = 0.0
    # Get a student's test scores.
    print("Student number", student + 1)
    print("-----------------")
    for test_num in range(num_test_scores):
        print("Test number", test_num + 1, end='')
        score = float(input(": "))
        # Add the score to the aaccumulator.
        total += score

    # Calculate the average test score for this student.
    average = total / num_test_scores

    # Display the average.
    print("The average for student number", student + 1, \
          "is:", average)

    print()
