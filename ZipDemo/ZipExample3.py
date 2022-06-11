name=["Nakul","Akash",'Peter']
marks=[70,80,90]
address=["ABC",'XYZ',"Demo"]
data=zip(name,marks,address)
mydata=list(data)

print(mydata)
a,b,c=zip(*mydata)
print(a)
print(b)
print(c)
