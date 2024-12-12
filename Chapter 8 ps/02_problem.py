# 2.
# Write a python program using function to convert Celsius to Fahrenheit.


Celsius = float(input("Enter the Celsus Degree: "))

def celsius_to_fahrenheit(Celsius):
    Fahrenheit = Celsius * (9/5) +32
    return Fahrenheit


print(celsius_to_fahrenheit(Celsius))