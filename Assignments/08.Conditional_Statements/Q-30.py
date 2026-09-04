age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
has_id_input = input("Do you have ID? yes/no: ")

has_id = has_id_input == "yes"

if age >= 18 and marks >= 40 and has_id is True:
    print("Eligible")
else:
    print("Not eligible")

print("and is appropriate because age, marks, and ID must all be valid together.")
