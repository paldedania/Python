# 5. Given person = {"name": "Ravi", "age": 21}, unpack it into a function with matching parameters.

def introduce(name, age):
    print(name, "is", age, "years old.")


person = {"name": "Ravi", "age": 21}
introduce(**person)
