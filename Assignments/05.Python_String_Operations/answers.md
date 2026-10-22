# Written answers

Source: https://github.com/codinggita/CGxSU_Semester_1/blob/main/Semester_1/python/05.Python_String_Operations/Assignment.md

## Theory

1. A string is an immutable Unicode sequence. Valid declarations include `name = 'Pal'`, `city = "Rajkot"` and triple-quoted multiline text. Encoding bytes in a file and Python's internal string representation are separate matters.
2. Zero-based indexing labels the first position 0; an index is the offset from the beginning.
3. Negative indexing counts from the end. `text[-1]` is the last character; `text[0]` is the first.
4. `[start:stop:step]` selects a sequence of positions. The stop index is excluded; the step cannot be zero.
5. Indexing selects one character, as in `text[0]`. Slicing selects a substring, as in `text[:3]`.
6. `len()` counts characters, including spaces.
7. Concatenation joins strings with `+`.
8. Repetition repeats a string with `*` and an integer.
9. A string's characters cannot be reassigned. `text[0] = "A"` raises `TypeError`; build a new string instead.
10. Both search for a substring's first index. A failed `find()` returns -1; a failed `index()` raises `ValueError`.
11. `upper()` uppercases letters; `lower()` lowercases them; `capitalize()` capitalizes the first character and lowercases the rest; `title()` applies title casing to words.
12. `strip()` returns text with surrounding whitespace removed; it does not remove internal spaces.
13. `split()` makes a list of pieces. `separator.join(pieces)` joins strings with the chosen separator.
14. `+` cannot concatenate a string and an integer. Use `"Age: " + str(age)` or an f-string.
15. `=` assigns a binding; `==` compares string values.

## Output answers

Assistant-generated expected outputs checked by execution. This does not record the learner making predictions before running code.

### Question 1

```text
P
h
n
o
```

Exact output: `'P\nh\nn\no\n'`

### Question 2

```text
Prog
gramm
Progr
amming
```

Exact output: `'Prog\ngramm\nProgr\namming\n'`

### Question 3

```text
Pto
yhn
nohtyP
```

Exact output: `'Pto\nyhn\nnohtyP\n'`

### Question 4

```text
11

d
```

Exact output: `'11\n \nd\n'`

### Question 5

```text
True
False
True
```

Exact output: `'True\nFalse\nTrue\n'`

### Question 6

```text
1
-1
3
```

Exact output: `'1\n-1\n3\n'`

### Question 7

```text
PYTHON
python
Python
Python
pYTHON
```

Exact output: `'PYTHON\npython\nPython\nPython\npYTHON\n'`

### Question 8

```text
I like Python
```

Exact output: `'I like Python\n'`

### Question 9

```text
Hello World
HelloHelloHello
```

Exact output: `'Hello World\nHelloHelloHello\n'`

For output Q8, `text` remains `"I like Java"`. `replace()` returns a new string.

Task 37 errors are `IndexError`, `TypeError`, `TypeError` and `ValueError`, in order. The corrections are in `Q-37.py`.
