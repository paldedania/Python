junior = 0
mid = 0
senior = 0
executive = 0
total = 0

for i in range(8):
    salary = float(input("Enter salary: "))
    total += salary
    if salary < 25000:
        print("Junior")
        junior += 1
    elif salary <= 50000:
        print("Mid")
        mid += 1
    elif salary <= 100000:
        print("Senior")
        senior += 1
    else:
        print("Executive")
        executive += 1

print("Junior:", junior)
print("Mid:", mid)
print("Senior:", senior)
print("Executive:", executive)
print("Average salary:", total / 8)
