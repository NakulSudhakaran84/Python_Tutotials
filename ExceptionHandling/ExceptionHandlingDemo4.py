try:
    num1=int(input("Please enter number 1 :"))
    num2=int(input("Please enter number 2 :"))
    result=num1/num2
    print(result)

except TypeError as err:
    print("Please provide only digits",err)

except ZeroDivisionError as err:
    print("Please do not enter zero ",err)

except ValueError as err:
    print("Please provide valid entry ",err)

except Exception as err:
    print("Something went wrong ",err)

else:
    print("All went right")

finally:
    print("Have a nice Day")

