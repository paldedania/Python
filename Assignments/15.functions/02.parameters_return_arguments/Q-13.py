# 13. Define classify_number(number) that returns "Positive", "Negative", or "Zero".

def classify_number(number):
    if number > 0:
        return "Positive"
    if number < 0:
        return "Negative"
    return "Zero"


print(classify_number(8))
print(classify_number(-3))
print(classify_number(0))
