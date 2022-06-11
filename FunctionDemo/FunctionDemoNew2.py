def print_names(**kwargs):
    print(kwargs)
    print(kwargs["address"])

print_names(name="Nakul",address="surabhi",phone=9089)



def hello_world(fname,*args,**kwargs):
    print(fname)
    print(args)
    print(kwargs)

hello_world(10,20,30,name="Python",country="India")