passed_students = 0
failed_students = 0
highest_percentage = 0
lowest_percentage = 0
first_student = True

for student in range(5):
    total = 0
    passed = True

    for subject in range(5):
        marks = int(input("Enter marks: "))
        total += marks
        if marks < 35:
            passed = False

    percentage = total / 5
    if passed:
        passed_students += 1
        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "E"
    else:
        failed_students += 1
        grade = "F"

    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

    if first_student or percentage > highest_percentage:
        highest_percentage = percentage
    if first_student or percentage < lowest_percentage:
        lowest_percentage = percentage
    first_student = False

print("Passed students:", passed_students)
print("Failed students:", failed_students)
print("Highest percentage:", highest_percentage)
print("Lowest percentage:", lowest_percentage)
