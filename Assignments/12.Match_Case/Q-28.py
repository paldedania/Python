choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Booking Ticket")
    case 2:
        print("Cancelling Ticket")
    case 3:
        print("Checking PNR")
    case 4:
        print("Opening Train Schedule")
    case 5:
        print("Exit Selected")
    case _:
        print("Invalid Choice")
