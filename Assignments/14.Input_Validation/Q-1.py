marks = int(input("Marks (0-100): "))

while marks < 0 or marks > 100:
    print("Invalid.")
    marks = int(input("Marks (0-100): "))

print("Marks:", marks)
