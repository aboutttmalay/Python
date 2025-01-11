# Write a class "calculator" capable of finding square, cube and square root of a
# number.

class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n}")
    
    def cube(self):
        print(f"The cube of the number is {self.n * self.n * self.n}")
    
    def square_root(self):
        print(f"The square root of the number is {self.n ** 0.5}")

# Taking user input
number = float(input("Enter the number: "))
a = calculator(number)
a.square()
a.cube()
a.square_root()