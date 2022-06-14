lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16]
]
#flatten_list=[]
#for sub_lst in lst:
#    for num in sub_lst:
#        flatten_list.append(num)
#print(max(flatten_list))
flt_list=[num for s_list in lst for num in s_list]
print(flt_list)
#num_gt_sixt=[num for num in flt_list if num>16]
#print(num_gt_sixt) filter
#odd_num=[num for num in flt_list if num%2!=0]
#print(odd_num)

#even_num=[num for num in flt_list if num%2==0]
#print(sum(even_num))
map_list=[num+1 if num>25 else num-1 for num in flt_list]#mapping
print(map_list)


