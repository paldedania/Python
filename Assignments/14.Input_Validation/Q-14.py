marks = int(input("Marks (0-100): "))

while marks < 0 or marks > 100:
    print("Invalid.")
    marks = int(input("Marks (0-100): "))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")
