secret_pin = 2468
correct_pin_entered = False

for attempt in range(1, 4):
    pin = int(input("PIN: "))
    if pin == secret_pin:
        correct_pin_entered = True
        break
    print("Wrong. Left:", 3 - attempt)

if correct_pin_entered:
    print("Access granted.")
else:
    print("Access denied.")
