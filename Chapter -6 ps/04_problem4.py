# 4. Write a program to find whether a given username contains less than 10
# characters or not.


username = input("Enter username : ")

if(len(username)<10):
    print("You username contains is less than 10 characters")
else:
    print("This username is valid")