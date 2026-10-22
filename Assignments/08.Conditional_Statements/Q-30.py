age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
has_id = input("Do you have ID? yes/no: ")

has_id = has_id.strip().lower() == "yes"
# All three requirements must hold, so combine them with and.

if age >= 18 and marks >= 40 and has_id is True:
    print("Eligible")
else:
    print("Not eligible")
