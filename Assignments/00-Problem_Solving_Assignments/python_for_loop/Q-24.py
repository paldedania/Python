sentence = input("Enter a sentence: ")
secret = input("Enter the secret word: ")
occurrences = 0
first_position = -1

if len(secret) > 0:
    for i in range(len(sentence) - len(secret) + 1):
        matches = True
        for j in range(len(secret)):
            if sentence[i + j] != secret[j]:
                matches = False
        if matches:
            occurrences += 1
            if first_position == -1:
                first_position = i

if occurrences > 0:
    print("Secret word found")
    print("Starting position:", first_position)
    print("Occurrences:", occurrences)
else:
    print("Secret word not found")
