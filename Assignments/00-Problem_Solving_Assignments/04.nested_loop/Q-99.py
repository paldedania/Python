# Q99. Exam Marks Analyzer
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
students = int(input())
subjects = int(input())
highest = None
best_student = 0
for student in range(students):
    marks = input().split()
    if len(marks) != subjects:
        raise ValueError("Enter one mark per subject")
    total = 0
    for subject in range(subjects):
        total += float(marks[subject])
    print("Student", student + 1, "Total =", total)
    if highest is None or total > highest:
        highest = total
        best_student = student + 1
if students:
    print("Highest total: Student", best_student, "=", highest)
