# Create a Class "Programmer" for storing information of few programmers
# working at Microsoft.


class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

# p = programmer("Malay",1200000,396445)
# print(p.company , p.name, p.salary, p.pin)

r = programmer
r.company = input("Enter the Company name: ")
r.name = input("Enter the name: ")
r.salary = int(input("Enter the salary: "))
r.pin = int(input("Enter the pin code for you: "))
print(r.company , r.name,r.salary,r.pin)