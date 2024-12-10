# Write a Python program that takes an integer input from the user and checks the following conditions:

# If the number is greater than 0, print "The number is positive."
# If the number is less than 0, print "The number is negative."
# If the number is exactly 0, print "The number is zero."


Number = int(input("Enter the number: "))

if(Number>0):
    print("The number is positive")
elif(Number<0):
    print("The number is negative")
else:
    print("The number is zero")


print("😊End of program!")