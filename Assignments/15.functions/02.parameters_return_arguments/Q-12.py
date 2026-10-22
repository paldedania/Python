# 12. Define count_digits(number) that returns the number of digits in a non-negative integer. For this exercise, treat 0 as having one digit.

def count_digits(number):
    if number == 0:
        return 1
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count


print(count_digits(0))
print(count_digits(12345))
