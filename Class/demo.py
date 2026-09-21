total = 0 
passed = True
grade = "" 
marks = 0
percentage = 0
skip = True 
for i in range(5):
    marks = int(input("Whats your marks? "))
    if marks > 100 or marks < 0:
        print("Enter properly")
        skip = False
    total += marks
    if marks <35:
        passed = False
if skip:
    if passed:
        percentage = total/5
        if percentage >=90:
            print("A")
        elif percentage > 80:
            print("B")
        elif percentage > 60:
            print("C")
        elif percentage > 50:
            print("D")
        else:
            print("F")

    if passed:
        print(total,percentage,"You have passed")
    else:
        print("You failed better luck next time!")