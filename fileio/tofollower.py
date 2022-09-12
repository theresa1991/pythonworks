import json
import random
try:
    with open("../blog/users.json") as f:#users.json in blog
        data=json.load(f)
        print(data)

        all_users=[user["id"]for user in data]
        my_followings=[user["followers"] for user in data if user["username"]=="akhil"][0]

        my_id=[user["id"] for user in data if user["username"]=="akhil"].pop()
#print(set(all_users))
#print(set(my_followings))
        to_follow=set(all_users)-set(my_followings)
        to_follow.remove(my_id)
        print(to_follow)
        suggestions=random.sample([*to_follow],2)#destructuring each value to list set is converted into list
        print(suggestions)
except Exception as e:
    print(e.__class__)