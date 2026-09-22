for i in range(5):
    username = input("Enter a username: ")

    digit_count = 0
    underscore_count = 0
    invalid_special = False
    first_is_letter = False

    if len(username) > 0:
        first = username[0]

        if (first >= "A" and first <= "Z") or (first >= "a" and first <= "z"):
            first_is_letter = True

    # Count digits and underscores, and find invalid characters
    for char in username:
        if char >= "0" and char <= "9":
            digit_count += 1
        elif char == "_":
            underscore_count += 1
        else:
            invalid_special = True

    if invalid_special:
        result = "Invalid"
    elif len(username) < 5 or first_is_letter == False:
        result = "Needs Improvement"
    else:
        result = "Valid"

    print("Length:", len(username))
    print("Digits:", digit_count)
    print("Underscores:", underscore_count)
    print("Result:", result)
