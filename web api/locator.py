#query to an address
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="desantoslocator")
location = geolocator.geocode("tamale")
print(location.address)
print("\n")
print((location.latitude, location.longitude))
print("\n")
print(location.raw)

#measuring distance
print("\n")
from geopy.distance import geodesic
tamale= (9.4043366, -0.8430289)
nugua = (8.4201854, -81.9890116)
print(geodesic(tamale, nugua).miles)

# using great-circle distance
print("\n")
from geopy.distance import great_circle
tamale = (9.4043366, -0.8430289)
nugua = (8.4201854, -81.9890116)
print(great_circle(tamale, nugua).miles)