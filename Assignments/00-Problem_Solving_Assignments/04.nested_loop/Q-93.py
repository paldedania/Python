# Q93. Digit Pair Analyzer
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
digits = str(abs(int(input())))
for first in digits:
    for second in digits:
        label = "Equal" if first == second else "Increasing" if first < second else "Decreasing"
        print(first, second, label)
