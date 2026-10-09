payment_type = int(input("Enter payment type (1=UPI, 2=Card, 3=Wallet): "))

match payment_type:
    case 1:
        option = int(input("UPI option (1=Scan QR, 2=Enter UPI ID): "))
        match option:
            case 1:
                print("Scan QR Selected")
            case 2:
                print("Enter UPI ID Selected")
            case _:
                print("Invalid UPI Option")
    case 2:
        option = int(input("Card option (1=Credit Card, 2=Debit Card): "))
        match option:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid Card Option")
    case 3:
        option = int(input("Wallet option (1=Add Money, 2=Pay Using Wallet): "))
        match option:
            case 1:
                print("Add Money Selected")
            case 2:
                print("Pay Using Wallet Selected")
            case _:
                print("Invalid Wallet Option")
    case _:
        print("Invalid Payment Type")
