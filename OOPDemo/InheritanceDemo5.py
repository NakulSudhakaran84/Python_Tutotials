class BaseClass:
    def hello_world(self):
        print("Hello Python from BaseClass")

class ChildClass(BaseClass):
    def hello_world(self):
        super().hello_world()
        #BaseClass.hello_world(self)
        print("Hello Python from ChildClass")

obj1=ChildClass()
obj1.hello_world()

