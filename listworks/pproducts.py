mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]
    ]
#q1 total number of out_of_stock mobiles
out_list=[mob for mob in mobiles if mob[-1]==0]
print(out_list)
# q2 total stock
tot_list=[mob for mob in mobiles if mob[-1]]
print(tot_list)
avail_list=sum([mob[-1]for mob in tot_list])
print(avail_list)
#q3 pritn mobiles available in range 20k to 30k
range_list=[mob for mob in mobiles if mob[4] in range(20000,30000)]
print(range_list)
# q4 print all 5g phone
fg_list=[mob for mob in mobiles if mob[2]=="5g"]
print(fg_list)
#print samsung mobiles
samsung_list=[mob for mob in mobiles if mob[-2]=="samsung"]
print(samsung_list)
#print costly mobile
cost_list=max(mobiles,key=lambda mob:mob[4])
print(cost_list)
#print lowest mobile
low_list=min(mobiles,key=lambda mob:mob[4])
# q8 print all mobiles having stock >10
ten_stock=[mob for mob in mobiles if mob[-1]>10]
print(ten_stock)
# q9 count of mobiles having dispaly amoled

amo_list=[mob for mob in mobiles if mob[3]=="AMOLED"]
count_list=[mob[3]for mob in amo_list]
print(len(count_list))
# q10 sort mobiles based on price oredr by desc
sort_list=mobiles.sort(reverse=True,key=lambda mob:mob[4])
print(sort_list)
