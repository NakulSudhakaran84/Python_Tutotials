class classA:
    def methodA(self):
        print("I am coming from Class A")

    def hello_world(self):
        print("Hello from Class A")


class classB(classA):
    def methodB(self):
        print("I am coming from Class B")

    def hello_world(self):
        print("Hello from Class B")



class classC(classB):
    def methodC(self):
        print("I am coming from Class C")


    def hello_world(self):
        print("Hello from Class C")


obj1=classC()
obj1.methodA()
obj1.methodB()
obj1.methodC()
obj1.hello_world()
