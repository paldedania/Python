# Largest of five
largest = float(input())
for i in range(4):
    number = float(input())
    if number > largest:
        largest = number
print(largest)
