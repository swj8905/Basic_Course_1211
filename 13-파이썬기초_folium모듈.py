from folium import Map

result = Map(location=[37.513399918743154, 127.10024155303084], zoom_start=17)
result.save("./map.html")