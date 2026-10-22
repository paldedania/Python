# 26. Define get_coordinates(x=0, y=0) that returns both values. Test default calls and calls with only one keyword argument.

def get_coordinates(x=0, y=0):
    return x, y


print(get_coordinates())
print(get_coordinates(x=5))
print(get_coordinates(y=7))
