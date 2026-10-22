# 6. Write a function with a docstring that explains its purpose, parameters, and return value.

def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Args:
        length: The rectangle's length.
        width: The rectangle's width, in the same unit as length.

    Returns:
        The rectangle's area in square units.
    """
    return length * width


print(calculate_area(5, 3))
print(calculate_area.__doc__)
