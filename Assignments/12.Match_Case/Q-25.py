ticket_type = int(input("Enter ticket type: "))

match ticket_type:
    case 1:
        ticket_name = "Regular Ticket"
    case 2:
        ticket_name = "Premium Ticket"
    case 3:
        ticket_name = "VIP Ticket"
    case _:
        ticket_name = None
        print("Invalid Ticket Type")

if ticket_name is not None:
    age = int(input("Enter age: "))
    if age < 5:
        print("Free Entry")
    else:
        print(f"{ticket_name} Selected")
