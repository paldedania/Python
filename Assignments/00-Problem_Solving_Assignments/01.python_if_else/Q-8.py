marks = int(input("Whats your marks: "))

if marks>=40 and marks<=100:
    print("Pass")
elif marks<40 and marks>=0:
    print("Fail")
else:
    print("Invalid marks")