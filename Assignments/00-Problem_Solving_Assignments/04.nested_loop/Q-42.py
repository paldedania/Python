# Q42. Longest and Shortest Word Pair
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
words = input().split()
if not words:
    print("No words")
else:
    # An outer candidate wins only after comparison with every other word.
    longest = words[0]
    shortest = words[0]
    for word in words:
        is_longest = True
        is_shortest = True
        for other in words:
            if len(other) > len(word):
                is_longest = False
            if len(other) < len(word):
                is_shortest = False
        if is_longest and len(word) > len(longest):
            longest = word
        if is_shortest and len(word) < len(shortest):
            shortest = word
    print("Longest =", longest)
    print("Shortest =", shortest)
