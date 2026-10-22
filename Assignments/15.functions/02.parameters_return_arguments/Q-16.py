# 16. Define format_name(first, last, uppercase=False). If uppercase is True, return the full name in uppercase.

def format_name(first, last, uppercase=False):
    full_name = first + " " + last
    if uppercase:
        return full_name.upper()
    return full_name


print(format_name("Asha", "Shah"))
print(format_name("Asha", "Shah", uppercase=True))
