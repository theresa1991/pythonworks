arr=[12,10,56,2,88,90,34]
low=0
upp=len(arr)-1
flag=0
element=100
while(low<=upp):
    mid=(low+upp)//2
    if element==arr[mid]:
        flag=1
        break
    elif element>arr[mid]:
        low=mid+1
    elif element<arr[mid]:
        upp=mid-1
print("found "if flag!=0 else "not found")