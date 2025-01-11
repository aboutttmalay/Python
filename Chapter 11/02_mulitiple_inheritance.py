

class Employee:
    company = 'Google'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(f"The name Employee is {self.name} and the salary is {self.salary}")

class Coder:
    language = 'Python'
    def printLangauge(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

class programmer(Employee , Coder):
    company = 'Microsoft'
    def show_Language(self):
        print(f"The name is {self.name} and he is good with {self.show_Language} language")


a = Employee("Alice", 100000)
b = programmer("Bob", 120000)


b.show()
b.printLangauge()
b.show_Language()