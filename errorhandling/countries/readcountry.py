#print total number of country details
import json
with open("county.json", encoding="UTF-8") as f :
    data=json.load(f)
print(len(data))

#print languages of ukraine
county_detail=[county["languages"] for county in data if county["name"]=="Ukraine"]
#print(county_detail)
for lan in county_detail[0]:#it contains double list
    print(lan["name"])

#print currency of china
china_cur=[county["currencies"] for county in data if county["name"]=="China"]
#print(china_cur)
chn_list=[cur["name"] for cur in china_cur[0]]
#print(chn_list)

#print population of india
india_pop=[county["population"] for county in data if county["name"]=="India"]
#print(india_pop)

#print neighboring countries of australia
aus_border=[county for county in data if county["name"]=="Australia"]
#print(aus_border)

def get_country(country_name):#for every country name
    return [country for country in data if country["name"].lower().startswith(country_name)]

country_data=get_country("india")
country_borders=country_data[0].get("borders")
sharing_borders=[country.get("name") for country in data if country["alpha3Code"]in country_borders]
print(sharing_borders)

#to print the country with maximum population
pop_list=max(data,key=lambda d:d.get("population"))
print(pop_list["name"])

pop_list=min(data,key=lambda d:d.get("population"))
print(pop_list["name"])