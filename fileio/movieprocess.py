# number of moviews released in 2022
movie=open("movies.txt")
all_movies=[]
for mov in movie:
    all_movies=[mov.rstrip("\n").split(",")for mov in movie]
mov_2022=[mov for mov in all_movies if mov[1]=="2022"]
print(len(mov_2022))
# number malayalam movies
mal_mov=[mov for mov in all_movies if mov[3]=="malayalam"]
print(len(mal_mov))
# theater released movies
theat_list=[mov for mov in all_movies if mov[-1]=="theater"]
print(theat_list)
# list of movies whose rating > 5
rating_list=[mov for mov in all_movies if mov[2]>"5"]
print(rating_list)

# {2022:,4,2021:6,2020:2}
movie_out={}
for mov in all_movies:
    year=mov[1]
    if year in movie_out:
        movie_out[year]+=1
    else:
        movie_out[year]=1
print(movie_out)
#maximum

#out=max(movie_out.items(),key=lambda ite:ite[1])
#print(out)