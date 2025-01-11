class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class manager(Programmer):
    c = 3

o = Employee() # # Prints the a attribute 
# print(o.b) Shows an error as there is no b attribute in Employee class
print(o.a)
o = Programmer()
print(o.a, o.b)
o = manager()
print(o.a, o.b, o.c)
