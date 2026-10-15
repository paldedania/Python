name = input("Enter a string: ")
already_printed = []

for char in name:
    if char not in already_printed:
        frequency = 0
        for other_char in name:
            if char == other_char:
                frequency += 1

        if frequency > 1:
            if frequency == 2:
                result = "Duplicate"
            elif frequency <= 4:
                result = "Repeated"
            else:
                result = "Highly Repeated"
            print(repr(char), frequency, result)
        already_printed.append(char)
