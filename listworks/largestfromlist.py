from functools import reduce
lst=[28,23,90,11,24,65]
str_lst=[str(n) for n in lst]
str_lst=sorted(str_lst,reverse=True)
print(str_lst)
max_num=reduce(lambda n1,n2:(n1+n2) if (n1+n2)>(n2+n1) else (n2+n1),str_lst)
print(max_num)