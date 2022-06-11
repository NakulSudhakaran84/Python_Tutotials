class Base:
    name="Nakul"
    def baseMethod(self):
        print("I am in Base class")

class Child(Base):
    company="Learn-Automation"
    def childMethod(self):
        print("I am in child class")

c=Child()
c.childMethod()
c.baseMethod()
print(c.name)
print(c.company)