def a():
    print("A")


def b():
    print("B")


a()
b()
a()

# Output:
# A
# B
# A
# Each call runs that function's body once.
