# 25. Define calculate_pay(hours, rate=200, bonus=0) that returns hours * rate + bonus. Try different combinations of positional and keyword arguments.

def calculate_pay(hours, rate=200, bonus=0):
    return hours * rate + bonus


print(calculate_pay(8))
print(calculate_pay(8, 250))
print(calculate_pay(8, bonus=500))
print(calculate_pay(8, 250, bonus=500))
