length = 0
sen = input("What is your sentence: ")
words = sen.split()

for i in words:
    if len(i) >6:
        print("Long")
    elif len(i) >= 4:
        print("medium")
    else:
        print("short")