age = int(input("Enter age: "))
has_id_input = input("Do you have ID? yes/no: ")

has_id = has_id_input == "yes"

if age >= 18 and has_id is True:
    print("Allowed")
