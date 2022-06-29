#word_count={"a":5,"b":3,"c":6,"t":9,"k":1}
#wc_list=word_count.items()#[("a":1,"b":2)]list of tuplespr
#print(sorted(wc_list,key=lambda item:item[1],reverse=True))
#print(max(wc_list,key=lambda item:item[1]))
#print(min(wc_list,key=lambda item:item[1]))

results = [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90 ,"A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win" :95, "A+": 50000},
    {"district":"mpm","win": 90,"A+": 4500}
    ]
print(sorted(results,key=lambda res:res["win"]))
aplus=[res["A+"] for res in results]
print(sum(aplus))