# 29. Define calculate_result(marks, passing_marks=35) that returns "Pass" if marks meet the passing mark and "Fail" otherwise.

def calculate_result(marks, passing_marks=35):
    if marks >= passing_marks:
        return "Pass"
    return "Fail"


print(calculate_result(35))
print(calculate_result(34))
print(calculate_result(45, passing_marks=50))
