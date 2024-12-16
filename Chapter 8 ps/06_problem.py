# Write a python function which converts inches to cms.



n = float(input("Enter the Inches : "))

def Inches_to_Centimeter(n):
    return n *(2.54)

InchestoCentimeter = Inches_to_Centimeter(n)
print(f"The {n} is Inches to centimeter: {InchestoCentimeter} inch")