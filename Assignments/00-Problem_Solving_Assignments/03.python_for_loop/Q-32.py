secret = input("Enter the secret password: ")

for i in range(5):
    attempt = input("Enter a password attempt: ")
    matching_characters = 0
    shorter_length = len(secret)

    if len(attempt) < shorter_length:
        shorter_length = len(attempt)

    for j in range(shorter_length):
        if secret[j] == attempt[j]:
            matching_characters += 1

    print("Matching characters:", matching_characters)
    same = len(secret) == len(attempt) and matching_characters == len(secret)
    if same:
        print("Correct")
    else:
        print("Incorrect")
