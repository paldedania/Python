age = int(input("Enter student age: "))
marks = float(input("Enter marks: "))
family_income = float(input("Enter family income: "))
attendance = float(input("Enter attendance percentage: "))

if age >= 18 and age <= 25 and marks >= 85 and attendance >= 75 and family_income <= 300000 and family_income >= 0:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")

    if age < 18 or age > 25:
        print("Reason: Age must be between 18 and 25")
    if marks < 85:
        print("Reason: Marks below 85")
    if attendance < 75:
        print("Reason: Attendance below 75%")
    if family_income > 300000:
        print("Reason: Family income above 300000")
    if family_income < 0:
        print("Reason: Invalid family income")
