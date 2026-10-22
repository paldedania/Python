# Q120. Final Multi-Level Data Analyzer
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
students = int(input())
subjects = int(input())
if students <= 0 or subjects <= 0:
    raise ValueError("Use positive student and subject counts")
subject_totals = [0] * subjects
subject_highs = [None] * subjects
subject_lows = [None] * subjects
subject_passes = [0] * subjects
grand_total = 0
passed_students = 0
highest_total = None
lowest_total = None
highest_mark = None
lowest_mark = None
for student in range(students):
    marks = input().split()
    if len(marks) != subjects:
        raise ValueError("Enter one mark per subject")
    total = 0
    passed = True
    student_high = None
    student_low = None
    for subject in range(subjects):
        mark = float(marks[subject])
        if not 0 <= mark <= 100:
            raise ValueError("Marks must be from 0 to 100")
        print("Student", student + 1, "Subject", subject + 1, "Mark =", mark)
        total += mark
        subject_totals[subject] += mark
        if mark >= 40:
            subject_passes[subject] += 1
        else:
            passed = False
        if subject_highs[subject] is None or mark > subject_highs[subject]:
            subject_highs[subject] = mark
        if subject_lows[subject] is None or mark < subject_lows[subject]:
            subject_lows[subject] = mark
        if student_high is None or mark > student_high:
            student_high = mark
        if student_low is None or mark < student_low:
            student_low = mark
        if highest_mark is None or mark > highest_mark:
            highest_mark = mark
        if lowest_mark is None or mark < lowest_mark:
            lowest_mark = mark
    average = total / subjects
    grade = "A" if average >= 90 else "B" if average >= 75 else "C" if average >= 60 else "D" if average >= 40 else "F"
    print("Student", student + 1, "Total =", total, "Average =", average)
    print("Highest mark =", student_high, "Lowest mark =", student_low)
    print("Result =", "Pass" if passed else "Fail", "Grade =", grade)
    if passed:
        passed_students += 1
    grand_total += total
    if highest_total is None or total > highest_total:
        highest_total = total
        topper = student + 1
    if lowest_total is None or total < lowest_total:
        lowest_total = total
        lowest_student = student + 1
for subject in range(subjects):
    print("Subject", subject + 1, "Total =", subject_totals[subject], "Average =", subject_totals[subject] / students)
    print("Highest =", subject_highs[subject], "Lowest =", subject_lows[subject])
    print("Pass =", subject_passes[subject], "Fail =", students - subject_passes[subject])
print("Grand total =", grand_total, "Class average =", grand_total / (students * subjects))
print("Highest total: Student", topper, "=", highest_total)
print("Lowest total: Student", lowest_student, "=", lowest_total)
print("Highest mark =", highest_mark, "Lowest mark =", lowest_mark)
print("Passed students =", passed_students, "Failed students =", students - passed_students)
print("Pass percentage =", passed_students / students * 100)
