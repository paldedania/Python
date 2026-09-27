table = 1
while table <= 5:
    multiplier = 1
    print("Table of", table)
    while multiplier <= 10:
        print(table, "x", multiplier, "=", table * multiplier)
        multiplier += 1
    print()
    table += 1
