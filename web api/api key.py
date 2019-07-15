import pyowm
 
location=input("what is your location?")
owm = pyowm.OWM('09a3954d276243deded1d4d4e3280a28')
observation = owm.weather_at_place(location)
w = observation.get_weather()
print(w)
 
print(w.get_wind()['deg'])
print(w.get_temperature())
print(w.get_humidity())
