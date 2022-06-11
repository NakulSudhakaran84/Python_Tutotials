class Person:

    def welcome(self):
        print("Hello Python")

    def hello_world(self):
        print("Hello world")

    def sum(self,num1,num2):
        print(num1+num2)

p=Person()
Person.welcome(p)
p.sum(12,34)

p.name="Nakul"
p.phone=9090898
p.country="India"

q=Person()
q.name="Akash"
q.phone=9887878
q.country="USA"

print(p.name)
print(q.name)