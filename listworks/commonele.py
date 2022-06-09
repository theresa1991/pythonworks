arr1=[13,16,10,6,49,900]
arr2=[111,90,34,55,9,1]
arr1.sort()
arr2.sort()
p1=0
p2=0
while(p1<len(arr1) and p2<len(arr2)):
    if arr1[p1]==arr2[p2]:
        print(f"common eleemnt {arr1[p1]}")
        p1+=1
        p2+=1
    elif arr1[p1]<arr2[p2]:
        p1+=1
    elif arr1[p1]>arr2[p2]:
        p2+=1
