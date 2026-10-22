# 22. Define calculate_stats(a, b, c) that returns the smallest, largest, and sum of three numbers.

def calculate_stats(a, b, c):
    return min(a, b, c), max(a, b, c), a + b + c


smallest, largest, total = calculate_stats(8, -2, 5)
print("Smallest:", smallest)
print("Largest:", largest)
print("Sum:", total)
