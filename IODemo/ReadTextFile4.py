import os

with open(os.path.dirname(os.getcwd())+"\\Demo1.txt") as f:                 #Context Manager
    print("Current state is ",f.closed)
    data=f.read()
    print(data)

print("State of the file is ",f.closed)