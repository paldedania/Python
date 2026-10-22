# Q78. Classroom Attendance Summary
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
students = int(input())
days = int(input())
best_student = 0
best_present = -1
for student in range(1, students + 1):
    attendance = input().upper().split()
    if len(attendance) != days:
        raise ValueError("Enter one P/A per day")
    present = 0
    absent = 0
    for day in range(days):
        if attendance[day] == "P":
            present += 1
        elif attendance[day] == "A":
            absent += 1
        else:
            raise ValueError("Use P or A")
    print("Student", student, "Present =", present, "Absent =", absent)
    if present > best_present:
        best_present = present
        best_student = student
if students > 0:
    print("Highest attendance: Student", best_student)
