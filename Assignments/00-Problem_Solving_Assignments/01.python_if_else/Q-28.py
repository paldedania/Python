name1 = input("Enter the first person's name: ")
age1 = int(input("Enter the first person's age: "))
name2 = input("Enter the second person's name: ")
age2 = int(input("Enter the second person's age: "))
name3 = input("Enter the third person's name: ")
age3 = int(input("Enter the third person's age: "))

if age1 < 0 or age2 < 0 or age3 < 0:
    print("Invalid age")
elif age1 == age2 and age2 == age3:
    print("All three people are the same age")
elif age1 == age2 and age1 < age3:
    print(name1, "and", name2, "are the youngest")
elif age1 == age3 and age1 < age2:
    print(name1, "and", name3, "are the youngest")
elif age2 == age3 and age2 < age1:
    print(name2, "and", name3, "are the youngest")
elif age1 < age2 and age1 < age3:
    print(name1, "is the youngest")
elif age2 < age1 and age2 < age3:
    print(name2, "is the youngest")
else:
    print(name3, "is the youngest")
