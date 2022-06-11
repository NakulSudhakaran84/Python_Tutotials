list1=[12,89,78,90]
list2=["Nakul",'Sudhakaran',"Python"]
list3="Nakul"

list1.extend(list2)
print(list1)

list1.extend(list3)
print(list1)

list1.extend('sudhakaran')
print(list1)

list1.pop()
print(list1)

list1.pop(6)
print(list1)

list2.remove('Nakul')
print(list2)