answers = [
    ("Stop searching after finding a username", "break"),
    ("Skip a blank string and process later strings", "continue"),
    ("Display Not found after a search finishes without a match", "for-else"),
    ("Keep an unfinished function syntactically valid", "pass"),
    ("Skip the current number but process later numbers", "continue"),
    ("Stop when a user enters a sentinel value", "break"),
    ("Report all items were checked without an early stop", "for-else"),
    ("Temporarily leave a conditional block empty", "pass"),
]

for situation, statement in answers:
    print(situation, ":", statement)
