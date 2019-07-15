from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="desantoslocator")
location = geolocator.geocode("nugua")
print(location.address)
print("\n")
print((location.latitude, location.longitude))