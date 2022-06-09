lst1=[11,12,13,14,15]
lst2=[11,14,15,16,17]
comlist=[]
# if n in lst2 returns true if n is present in list 2 else return false
for num in lst1:
    for n in lst2:
        if num==n:
            comlist.append(n)
print(comlist)