class classA:
    def methodA(self):
        print("I am coming from Class A")

    def hello_world(self):
        print("Hello from Class A")


class classB:
    def methodB(self):
        print("I am coming from Class B")

    def hello_world(self):
        print("Hello from Class B")



class classC(classB,classA):
    def methodC(self):
        print("I am coming from Class C")


    def hello_world(self):
        print("Hello from Class C")


c=classC()
c.methodA()
c.methodB()
c.methodC()
c.hello_world()
#c.hello_world2()
print(classC.mro())