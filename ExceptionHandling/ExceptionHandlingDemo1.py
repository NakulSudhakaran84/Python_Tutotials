try:
    content=open("C:\\Users\\Nakul Sudhakaran\\PycharmProjects\\Python_Tutotials\\Demo2.txt","r")
    print(content.read())
    print("Have a nice day")
except FileNotFoundError as err:
    print("Something went wrong ",err)

print("This is last statement")