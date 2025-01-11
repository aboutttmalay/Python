

class Employee:
    company = 'Google'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(f"The name Employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = 'Microsoft'
#     def show(self):
#         print(f"The name Programmer is {self.name} and the salary is {self.salary}")
#     def show_Language(self):
#         print(f"The name is {self.name} and he is good with {self.show_Language} language") 

class programmer(Employee):
    company = 'Microsoft'
    def show_Language(self):
        print(f"The name is {self.name} and he is good with {self.show_Language} language")


a = Employee("Alice", 100000)
b = programmer("Bob", 120000)
print(a.company, b.company)