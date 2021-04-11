import time

print('\n')
print("Welcome to Average Grade Calculator. Let's get to calculating...")

# List of user grades
grades = []

# Setting variable for while loop
ctn = 'y'

# Process for user to enter grades
while ctn == 'y':
    enter_grade = int(input("Enter you grade: "))
    grades.append(enter_grade)
    ctn = str(input("Do you want to enter another grade (y/n): "))

# Calculating the average based on the users input of grades
total_grades = sum(grades)
len_grades = len(grades)
average_grade = total_grades/len_grades
average_grade = round(average_grade)

# "Animation" of calculating the grade
print("Calculating Average Grade..")
time.sleep(1)
print('\n')

print("Average Grade: " + str(average_grade) + "%")