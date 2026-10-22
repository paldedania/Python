# 3. Define make_message(name, /, *, greeting="Hello"). Call it using valid and invalid argument styles.

def make_message(name, /, *, greeting="Hello"):
    return greeting + " " + name


print(make_message("Pal"))
print(make_message("Pal", greeting="Welcome"))

# name is positional-only; greeting is keyword-only.
try:
    make_message(name="Pal")
except TypeError:
    print("TypeError: name must be passed positionally.")

try:
    make_message("Pal", "Welcome")
except TypeError:
    print("TypeError: greeting must be passed by keyword.")
