# 17. Define percentage(marks, total=100) that returns the percentage. Assume total is not zero.

def percentage(marks, total=100):
    # The exercise assumes total is not zero.
    return marks / total * 100


print(percentage(85))
print(percentage(450, total=500))
