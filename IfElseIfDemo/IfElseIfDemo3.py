print("Welcome")
if 100>10:print("yes")
print("Bye")
print("****************")

print("yes") if 100>10 else print("no")

marks=95
print("A+") if marks>90 else print("A")

print("*************************************")

salary=input("Please eneter the salary for loan :")
sal=int(salary)
#sal=30000
if sal>40000:
    print("Eligible for car loan")
    if sal>80000:
        print("Eligible for home loan")
        if sal>100000:
            print("Premium customer- eligible for all kind of loan")

else:
    print("Sorry, we could not serve you")