def check_even_number(list1):
   even_number=[]

   for x in list1:
         if x%2==0:
             even_number.append(x)
         else:
             pass
   return even_number


result=check_even_number([1,3,4,6,8,32,64,99,87])
print(result)


def check_odd_number(list1):
   odd_number=[]

   for x in list1:
         if x%2==0:
             pass
         else:
             odd_number.append(x)
   return odd_number


result=check_odd_number([4,6,8,32,64])
print(result)

if len(result)>0:
    pass
else:
    print("Sorry no odd number found")
