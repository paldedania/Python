# 10. Define get_min_max(a, b) that returns both the smaller and larger values.

def get_min_max(a, b):
    if a <= b:
        return a, b
    return b, a


smallest, largest = get_min_max(10, 4)
print("Smallest:", smallest)
print("Largest:", largest)
