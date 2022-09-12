import json
import functools
import random

with open("songs.json") as f:
    data = json.load(f)
# print total number of songs in album1
num_song = [song for song in data if song["album"] == "album1"]
print(len(num_song))

albm_count = list(filter(lambda song: song["album"] == "album1", data))
print(len(albm_count))

# sad mode songs with random sample of 2
sad_songs = [s for s in data if s["mode"] == "sad"]
print(random.sample(sad_songs, 2))

# total number of albums
tot_num = set([s["album"] for s in data])
print(len(tot_num))

# which album contains most songs
sc = {}
for song in data:
    album_name = song.get("album")
    if album_name in sc:
        sc[album_name] += 1
    else:
        sc[album_name] = 1
print(sc)
print(max(sc.items(), key=lambda s: s[1]))

# list of top rated songs
top_song = max(data, key=lambda s: s["rating"])
print(top_song["rating"])
topsong_list = [s for s in data if s["rating"] == top_song["rating"]]
print(topsong_list)
# top_song=functools.reduce(lambda s1,s2:s1 if s1["rating"]>s2["rating"] else s2,data)
# print(top_song)
