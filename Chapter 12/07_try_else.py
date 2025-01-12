try:
    a = int(input("Hey,Enter the a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else ")


'''

Syntax of try and else

try:
    # Somecode
except :
    # Somecode
eIse:
    # Code
    # This is executed only if the try was successful
'''