from geopy.extra.rate_limiter import RateLimiter
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
from geopy import distance
geolocator = Nominatim(user_agent="name")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=2)


# folium polyline


PATH = "location.list"
films = []
suitable_films = []

year = input("Please enter a year you would like to have a map for: ")
current_lat, current_long = [float(x) for x in input(
    "Please enter your location (format: lat, long):").split(",")]

print("Map is generating...")
print("Please wait...")


with open(PATH, "r") as films_locations:
    for film in films_locations:
        films.append(film.split("\t"))
for flm in films:
    if flm[1] == year:
        suitable_films.append(flm)


for point in suitable_films:
    try:
        location = geolocator.geocode(point[2])
        film_location = (location.latitude, location.longitude)
        point.append(film_location)
        dist = distance.geodesic((current_lat, current_long), film_location).km
        point.append(dist)

    except AttributeError:
        continue
    except GeocoderUnavailable:
        continue


filtered_suitable_films = list(
    filter(lambda lst: len(lst) == 5, suitable_films))

sorted_films = sorted(filtered_suitable_films, key=lambda x: x[-1])

final_film_lst = sorted_films[:10]

my_location = (current_lat, current_long)

# Folium Part
map = folium.Map(location=my_location, zoom_start=3)


map.add_child(folium.Marker(location=my_location,
                            popup="Your location",
                            icon=folium.Icon(color='red', icon='home')))


flms = folium.FeatureGroup(name="films")
for film_lst in final_film_lst:
    title = film_lst[0]
    distance_from_given_point = film_lst[4]
    coordinates = film_lst[3]

    flms.add_child(folium.Marker(location=coordinates,
                                 popup=f"Titile: {title}, \n Distance from given point: {round(distance_from_given_point, 2)} km",
                                 icon=folium.Icon(color='cadetblue')))

    folium.PolyLine(((my_location), (coordinates)), color='gray').add_to(map)

map.add_child(flms)
map.save(f"{year}_movies_map.html")

print(f"Finished. Please have look at the map {year}_movies_map.html")
