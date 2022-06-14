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
# q1 total number of out_of_stock mobiles

st_list=[mob for mob in mobiles if mob[6]==0]
print(len(st_list))
# q2 total stock
avl_stock=[mob[-1] for mob in mobiles]
print(sum(avl_stock))

# q3 pritn mobiles available in range 20k to 30k
mobile_range=[mob for mob in mobiles if mob[4] in range(20000,30000)]
print(mobile_range)
# q4 print all 5g phone
mobile_5g=[mob for mob in mobiles if mob[2]=="5g"]
print(mobile_5g)

# q5 print samsung mobiles
mobiles_samsung=[mob for mob in mobiles if mob[-2]=="samsung"]
print(mobiles_samsung)
# q6 print costly mobile
#mobiles_max=max([mob[4] for mob in mobiles])
#print(mobiles_max)
#costly_price=[mob for mob in mobiles if mob[4]==mobiles_max]
#print(costly_price)
#max_list=mobiles.sort(reverse=True,key=lambda mob:mob[4])
costly_list=max(mobiles,key=lambda mob:mob[4])
print(costly_list)


# q7 prin low cost mobiles
low_list=min(mobiles,key=lambda mob:mob[4])
print(low_list)
# q8 print all mobiles having stock >10
stockl_st=[mob for mob in mobiles if mob[-1]>10]
print(stockl_st)


# q9 count of mobiles having dispaly amoled

# q10 sort mobiles based on price oredr by desc

# q11 sort mobiles based on avl stock oredr by desc

# q12 is there any mobile available at rs 10000 ?
mob_ten=[mob[4]==10000 for mob in mobiles]#returns a boolean mob[4]==10000 true or false if available true else false
print("available" if True in mob_ten else "na")
# q12 list all mobiles having same price
