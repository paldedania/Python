for student in range(7):
    present_days = 0

    for day in range(5):
        attendance = input("Enter P or A: ").upper()
        if attendance == "P":
            present_days += 1

    percentage = present_days * 100 / 5
    if percentage >= 90:
        result = "Excellent"
    elif percentage >= 75:
        result = "Good"
    else:
        result = "Warning"

    print("Student", student + 1, "attendance:", present_days, "days")
    print("Percentage:", percentage)
    print(result)
