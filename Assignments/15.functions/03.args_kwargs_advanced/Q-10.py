# 10. Explain the difference between *args in a function definition and *values in a function call.

def show_arguments(*args):
    # In a definition, *args collects positional arguments into a tuple.
    print(args)


values = [4, 5, 6]
# In a call, *values unpacks an iterable into separate positional arguments.
show_arguments(*values)  # args is (4, 5, 6).
show_arguments(values)  # args is ([4, 5, 6],), a tuple holding one list.
