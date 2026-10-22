# 9. What happens if the same parameter gets a value both positionally and through **kwargs?

# A regular parameter cannot receive both a positional and a keyword value.
# The call fails with TypeError before the function body runs.
def greet(name, **kwargs):
    print("Hello", name)


try:
    greet("Asha", **{"name": "Ravi"})
except TypeError:
    print("TypeError: multiple values for argument 'name'.")

# Fix: supply name once. Other keywords can still go into kwargs.
greet("Asha", city="Pune")
