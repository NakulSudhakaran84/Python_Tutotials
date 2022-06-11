def print_name(*args):
    print(args)

    for a in args:
        print(a)
print_name("python","java")



def get_sum_of_all_numbers(*args):
    print(sum(args))

    print(min(args))
    print(max(args))


get_sum_of_all_numbers(10,30,60)
