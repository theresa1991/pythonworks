mobile=open("mobiles.txt")
all_mobiles=[]
for mob in mobile:
    #print(mob)
    all_mobiles=[mob.rstrip("\n").split(",")for mob in mobile]
    #all_mobiles.append(mobile_list)
#print(all_mobiles)
costly_mob=max(all_mobiles,key=lambda mobi:mobi[2])
print(costly_mob)
five_g=[mobi for mobi in all_mobiles if mobi[3]=="5g"]
print(five_g)
