with open("Demo.txt") as f:                 #Context Manager
    print("Current state is ",f.closed)
    data=f.read()
    print(data)

print("State of the file is ",f.closed)