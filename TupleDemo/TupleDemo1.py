tup1=(1,"Python",90.0,True,1,1,1,"QA")
print(tup1)

print(tup1[1])
print(tup1[-2])

print(tup1.count(0)) #True is counted as 1 False is counted as 0

print(tup1.index(90.0))
print(tup1[0:4])

#tup1[0]="Nakul"     #Tuple wont allow to append item. Tuple is immutable
#print(tup1)