try:
    f=open("Demo.txt")
    data=f.read()
    print(data)
    print(f.name)
    print(f.mode)



except Exception as err:
    print("Exception is",err)

finally:
    f.close()