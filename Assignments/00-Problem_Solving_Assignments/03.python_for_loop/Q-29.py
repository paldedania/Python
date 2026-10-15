for i in range(5):
    email = input("Enter an email-like string: ")
    at_count = 0
    at_position = -1
    has_space = False

    for j in range(len(email)):
        if email[j] == "@":
            at_count += 1
            at_position = j
        if email[j] == " ":
            has_space = True

    has_dot_after_at = False
    if at_position >= 0:
        for j in range(at_position + 1, len(email)):
            if email[j] == ".":
                has_dot_after_at = True

    before_at_exists = at_position > 0
    domain_exists = at_position >= 0 and at_position < len(email) - 1

    if at_count == 1 and has_dot_after_at and not has_space and before_at_exists and domain_exists:
        print("Valid")
    else:
        print("Invalid")
