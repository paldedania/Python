# Q73. Student Marks Matrix
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
# Enter one row of four marks per student.
for student in range(1, 4):
    marks = input().split()
    if len(marks) != 4:
        raise ValueError("Enter four marks per student")
    total = 0
    for subject in range(4):
        mark = float(marks[subject])
        print("Student", student, "Subject", subject + 1, "=", mark)
        total += mark
    print("Total =", total, "Average =", total / 4)
