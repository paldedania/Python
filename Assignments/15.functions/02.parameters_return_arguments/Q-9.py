# 9. Define subtract(a, b) and show how changing positional argument order changes the result.

def subtract(a, b):
    return a - b


print(subtract(10, 3))  # 7
print(subtract(3, 10))  # -7: reversing the arguments changes a and b.
