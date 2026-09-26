name = input("Enter the string: ")
if len(name) > 0:
    current_char = name[0]
    count = 1

    for i in range(1, len(name)):
        if name[i] == current_char:
            count += 1
        else:
            print(current_char, count, sep="", end="")
            current_char = name[i]
            count = 1

    print(current_char, count, sep="")
