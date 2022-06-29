weather=[
    {"district": "tvm", "temp":30},
    {"district": "ktm","temp":28 },
    {"district": "apy","temp":27},
    {"district": "idk","temp":18 },
    {"district": "ekm","temp":31 },
    {"district": "pta","temp":21},
    {"district": "tsr","temp":24},
    {"district": "kzd","temp":29},
    {"district": "pkd","temp":34},
    {"district": "mpm","temp":31},
    {"district": "tvm", "temp": 31},
    {"district": "ktm", "temp": 29},
    {"district": "apy", "temp": 26},
    {"district": "idk", "temp": 20},
    {"district": "ekm", "temp": 30},
    {"district": "pta", "temp": 22},
    {"district": "tsr", "temp": 27},
    {"district": "kzd", "temp": 28},
    {"district": "pkd", "temp": 30},
    {"district": "mpm", "temp": 29},

]
#out={"tvm":31,"ktm":29,}
out={}
for data in weather:
    dist_name=data["district"]
    cur_temp=data["temp"]
    if dist_name in out:
        old_temp=out[dist_name]
        if cur_temp>old_temp:
            out[dist_name]=cur_temp
    else:
        out[dist_name]=cur_temp
print(out)
# sort out based on temparature
print(sorted(weather,key=lambda temp1:temp1["temp"]))
# find max tem district
print(max(weather,key=lambda temp1:temp1["temp"]))
# find min tem district
print(min(weather,key=lambda temp1:temp1["temp"]))
# dictionary methods