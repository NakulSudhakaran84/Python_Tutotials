status=False
names=["Python","Java","JS","CSharp"]

for name in names:
    if name=="JS":
        status=True
        break
    else:
        print("Please wait we are still searching")

if status:
    print("We are glad that we found the record")
else:
    print("Sorry we could not found the record")
