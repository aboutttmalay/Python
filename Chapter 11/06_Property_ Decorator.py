class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, name):
        self.fname, self.lname = name.split(" ")


e = Employee()
e.a = 45
e.name = "Harry Potter"
print(e.name)
e.show()