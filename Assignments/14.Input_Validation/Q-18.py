month = int(input("Month (1-12): "))
while month < 1 or month > 12:
    print("Invalid.")
    month = int(input("Month (1-12): "))

day = int(input("Day (1-31): "))
while day < 1 or day > 31:
    print("Invalid.")
    day = int(input("Day (1-31): "))

print("Date:", month, day)
