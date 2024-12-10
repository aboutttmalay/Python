# Write a program which finds out whether a given name is present in a list or not.
list_of_name = ["malay", "manav" , "moti" , "vasu" , "kunj" , "mohit"]

name  = input("Enter the name: ")

if(name in list_of_name):
    print("This name is present in list")
else:
    print("This name is not present")