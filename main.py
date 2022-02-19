import phonenumbers

import folium

from test import number

from phonenumbers import geocoder
Key = "dca14f2b9b7a4605967cbaaef2d2d99e"
samNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)


lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng],popup = yourLocation).add_to((myMap))

myMap.save("myLocation.html")