import folium
map = folium.Map()

year = int(input("Please enter a year you would like to have a map for: "))
current_lat, current_long = [int(x) for x in input("Please enter your location (format: lat, long):").split(",")]
print([current_lat, current_long])





map.add_child(folium.Marker(location=[current_lat, current_long],
                            popup="Joe Louis Arena, Steve Yzerman Drive, Detroit, Wayne County, Michigan, 48226, United States",
                            icon = folium.Icon()))
# map.save("Map_1 .html")

print()


