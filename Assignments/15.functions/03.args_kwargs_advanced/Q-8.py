# 8. Explain why type hints alone do not prevent a function from receiving a value of the wrong type.

# Type hints describe expected types for readers, editors and type checkers.
# Python does not enforce them automatically at runtime.
def square(number: int) -> int:
    return number * number


print(square(2.5))  # 6.25, even though the hint says int.
