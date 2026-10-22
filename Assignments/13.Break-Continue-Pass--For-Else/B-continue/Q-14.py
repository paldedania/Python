marks = input("Enter marks separated by spaces: ").split()
printed_a_mark = False

for item in marks:
    mark = int(item)
    if mark < 40:
        continue
    print(mark, end=" ")
    printed_a_mark = True

print()
