# Programing exercises
# 14.Body Mass Index

# This program calcualte and display a person's
# body mass inde.
print("***Body Mass Index***")

# Get the user input
weight = float(input("Please enter your weight(pounds): "))
height = float(input("Please enter your height(inches): "))

# Calculate the BMI base on user's input
BMI = weight * 703 / (height*height)

# Detemine overweight and print the result.
if (BMI >= 18.5 and BMI <= 25):
    print("Your BMI = ", format(BMI, '.2f'),
          ". You are optimal.", sep='')

elif (BMI < 18.5):
    print("Your BMI = ", format(BMI, '.2f'),
          ". You are underweight.", sep='')

elif (BMI > 25):
    print("Your BMI = ", format(BMI, '.2f'),
          ". You are overweight.", sep='')

else:
    print("Your BMI = ", format(BMI, '.2f'),
          ". Sorry, please enter again.", sep='')
