lst=[2,3,4,6,8,7,5,]
#sum=12
#for i in range(0,len(lst)):
 #   for j in range(i+1,len(lst)):
 #       cu_sum=lst[i]+lst[j]
 #       if cu_sum==sum:
 #           print(f"pairs{lst[i]},{lst[j]}")
  #          break
lst.sort()
low=0
upp=len(lst)-1
element=7
while(low<upp):
    curr_sum=lst[low]+lst[upp]
    if element==curr_sum:
        print(f"Pairs {lst[low]},{lst[upp]}")
        break
    elif curr_sum>element:
        upp-=1
    elif curr_sum<element:
        low+=1