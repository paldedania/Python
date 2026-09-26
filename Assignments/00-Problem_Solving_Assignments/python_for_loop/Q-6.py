for i in range(5):
    number = int(input("Enter a number: "))
    number_string = str(number)
    even_count = 0
    odd_count = 0

    for char in number_string:
        if char == "-":
            continue
        if int(char) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Number as string:", number_string)
    print("Even digits:", even_count)
    print("Odd digits:", odd_count)
    if even_count > odd_count:
        print("Even occurs more")
    elif odd_count > even_count:
        print("Odd occurs more")
    else:
        print("Equal")
