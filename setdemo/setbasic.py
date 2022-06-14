#lst={1,1,2,3,1,2,89,23,23,45,67,90,78}
#st=set(lst)
#print(st)
st1={1,2,3,4,5}
st2={4,5,6,7,8}
#union_set=st1.union(st2)
#print(union_set)
#intersection_set=st1.intersection(st2)
#print(intersection_set)
#diff_set=st1.difference(st2)
#print(diff_set)
#students=["ram","ravi","hari","tom","nikil","anna"]
#failed_st=["ram","ravi","hari"]
#diff_st=set(students).difference(set(failed_st))
#print(diff_st)
laptop={"name":"hp","memory":"32gb","storage":"256GB","display":"13.3inch"}
print(laptop["name"])
print(laptop["storage"])
print(laptop["memory"])
print(laptop["display"])
print("CPU"in laptop)
laptop["cpu"]="intel i5"
print(laptop)
laptop["name"]="dell"
print(laptop)