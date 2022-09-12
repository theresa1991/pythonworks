import json
with open("posts.json",encoding="UTF-8")as f:
    data=json.load(f)
    #print(len(data))
#number of post by user id 1
id_list=[d for d in data if d["userId"]==1]
print(len(id_list))
#total number of likes for postId 6
like_list=[len(d["liked_by"]) for d in data if d["postId"]==6]
print(like_list)

#number posts liked by user=2
like_count=len([d for d in data if 2 in d["liked_by"]])
print(like_count)

