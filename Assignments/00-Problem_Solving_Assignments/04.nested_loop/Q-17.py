# Q17. Multiples Detector
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
for i in range(1, n + 1):
    line = ""
    for j in range(1, n + 1):
        if j % i == 0:
            if line:
                line += " "
            line += str(j)
    print(line)
