fail = 0
passed = 0
good = 0
excellent = 0
for i in range(10):
    marks = int(input("What are your marks?: "))
    if marks<0 or marks>100:
        print("error its wrong this wont count")
    elif marks >= 75:
        print("Excellent")
        excellent +=1
    elif marks >= 50:
        print("Good")
        good +=1
    elif marks >= 35:
        print("Pass")
        passed+=1
    else:
        print("Fail")
        fail+=1
print(f"in 75-100 there are {excellent} then in 50-74 there are {good} then in 35-49 there are {passed} then who failed are {fail}")
