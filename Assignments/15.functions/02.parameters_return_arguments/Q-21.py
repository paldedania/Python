# 21. Define analyze_number(number) that returns three values: the absolute value, whether it is even, and the number of digits. Do not use abs(); assume the input is an integer.

def analyze_number(number):
    positive_number = number
    if positive_number < 0:
        positive_number = -positive_number

    digits = 1
    remaining = positive_number
    while remaining >= 10:
        digits += 1
        remaining //= 10

    return positive_number, number % 2 == 0, digits


print(analyze_number(-246))
print(analyze_number(0))
