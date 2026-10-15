score_1 = int(input("Score 1: "))
while score_1 < 0 or score_1 > 100:
    print("Invalid.")
    score_1 = int(input("Score 1: "))

score_2 = int(input("Score 2: "))
while score_2 < 0 or score_2 > 100:
    print("Invalid.")
    score_2 = int(input("Score 2: "))

score_3 = int(input("Score 3: "))
while score_3 < 0 or score_3 > 100:
    print("Invalid.")
    score_3 = int(input("Score 3: "))

total = score_1 + score_2 + score_3
average = total / 3
print("Total:", total)
print("Average:", average)
