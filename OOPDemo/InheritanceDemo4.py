class A:
    def sum(self):
        print("Calling fro A-sum of two numbers is 15")

class B(A):
    def sum(self):
        print("Calling from B-sum of two numbers is 25")

class C(B):
    def sum(self):
        print("Calling from C-sum of two numbers is 50")


#obj1=A()
#obj1.sum()

obj2=C()
obj2.sum()