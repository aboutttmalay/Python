class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
        super().__init__()
    b = 2

class Manager(Programmer):
    def __init__(self):
        print("Constructor of Manager")
        super().__init__()
    c = 3

# o = Employee() # # Prints the a attribute 
# # print(o.b) Shows an error as there is no b attribute in Employee class
# print(o.a)




# o = Programmer()
# print(o.a, o.b)





# o = manager()
# print(o.a, o.b, o.c)
