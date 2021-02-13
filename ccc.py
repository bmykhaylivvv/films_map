PATH = "location.list"

films = []

with open(PATH, "r") as films_location:
    for line in films_location:
        films.append(line.split("\t"))


print(films[10][2])


from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="name")

location = geolocator.geocode(films[321][2])

print(location.address)

print((location.latitude, location.longitude))