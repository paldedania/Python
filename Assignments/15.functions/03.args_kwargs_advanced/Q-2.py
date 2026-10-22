# 2. Write print_profile(**kwargs) that prints each key and value on a separate line.

def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)


print_profile(name="Pal", age=18, city="Ahmedabad")
