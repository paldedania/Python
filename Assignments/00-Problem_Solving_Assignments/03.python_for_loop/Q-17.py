highest_marks = 0
highest_student = ""

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    vowels = 0
    consonants = 0

    for char in name.lower():
        if char in "aeiou":
            vowels += 1
        elif char >= "a" and char <= "z":
            consonants += 1

    print("Grade:", grade)
    print("Vowels:", vowels)
    print("Characters:", len(name))

    if vowels > consonants:
        print("The name has more vowels")
    elif consonants > vowels:
        print("The name has more consonants")
    else:
        print("The name has equal vowels and consonants")

    if marks > highest_marks:
        highest_marks = marks
        highest_student = name

    print()

print("Student with highest marks:", highest_student)
print("Highest marks:", highest_marks)