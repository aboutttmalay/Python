# 6. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F


marks1 = int(input("Enter the marks1: "))
marks2 = int(input("Enter the marks2: "))
marks3 = int(input("Enter the marks3: "))
marks4 = int(input("Enter the marks4: "))
marks5 = int(input("Enter the marks5: "))

total_percentage = (100 *(marks1+marks2+marks3+marks4+marks5) ) / 500
if(total_percentage>=90 and total_percentage<=100):
    print("You grade is Excllent")
elif(total_percentage>=80 and total_percentage<=90):
    print("You Grade is A")
elif(total_percentage>=70 and total_percentage<=80):
    print("You grade is B")
elif(total_percentage>=60 and total_percentage<=70):
    print("You grade is c")
elif(total_percentage>=50 and total_percentage<=60):
    print("You grade is D")
elif(total_percentage<=50):
    print("You are failed,Try again next year! ")
