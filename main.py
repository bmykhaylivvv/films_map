from geopy.extra.rate_limiter import RateLimiter
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
from geopy import distance
geolocator = Nominatim(user_agent="name")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=2)


# folium polyline


map = folium.Map()

PATH = "location.list"
films = []
suitable_films = []

year = input("Please enter a year you would like to have a map for: ")
current_lat, current_long = [int(x) for x in input(
    "Please enter your location (format: lat, long):").split(",")]


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

final_film_lst = sorted_films[:9]



# Folium Part
me = folium.FeatureGroup(name="me")


flms = folium.FeatureGroup(name="films")
for film_lst in final_film_lst:
    title = film_lst[0]
    distance_from_given_point = film_lst[4]
    coordinates = film_lst[3]

    # flms.add_child(folium.Marker(location=(41.8755616, -87.6244212),
    #                             popup=f"Your`re here",
    #                             icon=folium.Icon(color='red')))

    flms.add_child(folium.Marker(location=coordinates,
                                popup=f"Titile: {title}, \n Distance from given point: {distance_from_given_point}",
                                icon=folium.Icon(color='cadetblue')))

map.add_child(flms)
map.save("Map_1 .html")
# (41.8755616, -87.6244212)