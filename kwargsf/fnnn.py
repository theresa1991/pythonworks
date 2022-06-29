def max_fn(*args):
    return max(args)

def min_fun(*arg):
    return min(arg)

def sum_fn(*args):
    return sum(args)
print(max_fn(45,12,456,90))
print(min_fun(45,12,456,90))
print(sum_fn(45,12,456,90))

def add_num(**kwargs):
    print(kwargs)
    print(sum([v for k, v in kwargs.items()]))



add_num(n1=12,n2=90,n3=99)
