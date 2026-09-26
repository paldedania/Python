words = input("Enter a sentence: ").lower().split()
already_printed = []

for word in words:
    if word not in already_printed:
        frequency = 0
        for other_word in words:
            if word == other_word:
                frequency += 1

        if frequency > 1:
            print(word, frequency)
        already_printed.append(word)
