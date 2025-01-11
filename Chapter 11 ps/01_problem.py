# 1. Create a class (2-D vector) and use it to create another class representing a 3-D
# vector.

class twoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")
    

class threeDvector(twoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


i = int(input("Enter the i component of the 2-D vector: "))
j = int(input("Enter the j component of the 2-D vector: "))
k = int(input("Enter the k component of the 3-D vector: "))
v2 = twoDvector(i, j)
v2.show()
v3 = threeDvector(i, j, k)
v3.show()
