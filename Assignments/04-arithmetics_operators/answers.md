# Written answers

Source: https://github.com/codinggita/CGxSU_Semester_1/blob/main/Semester_1/python/04.Arithmetic_Operators/Assignment.md

## Theory

1. `+` adds, `-` subtracts, `*` multiplies, `/` divides, `//` floors a quotient, `%` gives a remainder and `**` raises a value to a power.
2. For the numbers here, `/` produces a floating-point quotient; `//` rounds toward negative infinity. An integer pair with `//` produces an integer; a float operand produces a float.
3. The floor is the greatest integer no larger than the quotient. The quotient is about -3.333, whose floor is -4.
4. The remainder satisfies `a == (a // b) * b + a % b`. Here `-10 == -4 * 3 + 2`, so the remainder is 2.
5. Subtracting negative five adds five, giving 15.
6. Precedence decides which operations bind first. Multiplication gives 10 before addition gives 20.
7. Parentheses group addition first. The results are 20 and 30.
8. `**` is exponentiation. `-2 ** 2` is `-(2 ** 2)`, giving -4; `(-2) ** 2` gives 4.
9. Booleans act as integers 1 and 0 in arithmetic. Most arithmetic results are int; `/` produces float.
10. `None` is an absence marker. Numeric arithmetic with it raises `TypeError`.
11. `+` joins strings and `*` repeats a string by an integer. The results are `HelloWorld` and `HelloHelloHello`.
12. Division by zero raises `ZeroDivisionError`.

## Output answers

Assistant-generated expected outputs checked by execution. This does not record the learner making predictions before running code.

The nonzero modulus result has the divisor's sign. Floor division rounds downward rather than truncating toward zero. The practical scripts demonstrate deliberate errors with their exception names.
