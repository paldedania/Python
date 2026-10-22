# 28. Define convert_temperature(value, scale="C"). If scale is "C", convert Celsius to Fahrenheit; if "F", convert Fahrenheit to Celsius. Return the converted value. Assume the scale is valid.

def convert_temperature(value, scale="C"):
    if scale == "C":
        return value * 9 / 5 + 32
    return (value - 32) * 5 / 9


print(convert_temperature(0))
print(convert_temperature(212, scale="F"))
