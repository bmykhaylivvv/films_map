import folium
from geopy.geocoders import Nominatim

PATH = "location.list"

films = []

with open(PATH, "r") as films_location:
    for line in films_location:
        films.append(line.split("\t"))


print(films[10][2])



geolocator = Nominatim(user_agent="name")

location = geolocator.geocode(films[321][2])

# print(location.address)

print((location.latitude, location.longitude))

map = folium.Map()

map.add_child(folium.Marker(location=(location.latitude, location.longitude),
                            popup=f"Titile:",
                            icon=folium.Icon(color='red')))


map.add_child(folium.Marker(location=(45, 34),
                            popup=f"Titile:",
                            icon=folium.Icon(color='cadetblue')))

# map.save("Map_1 .html")
help(folium.Icon)

