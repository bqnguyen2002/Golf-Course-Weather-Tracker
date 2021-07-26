# Python program to find current
# weather details of any golf course given the golf course name
# using openweather api and golf course api
# import required modules
import requests, json

#Enter the golf club name and finds the city 
GOLF_CLUB = input("Enter the Golf Club name: ")
GOLF_URL = "http://www.golfworldapi.com/api/bv1/Clubs?" + "golfclub=" + GOLF_CLUB
responseGolf = requests.get(GOLF_URL)
golf_data = responseGolf.json()
CITY = golf_data[0]['ClubCity']

# Enter your API key here
API_KEY = "417b920b02aa057868f49d0b740636be"

#Enter the units for temperature
UNIT = "imperial"

WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?" + "q=" + CITY + "&units=" + UNIT + "&appid=" + API_KEY

# HTTP request
responseWeather = requests.get(WEATHER_URL)

# checking the status code of the request
if responseWeather.status_code & responseGolf.status_code == 200:

   # getting data in the json format
   weather_data = responseWeather.json()

   print(f"{CITY:-^30}")
   print(f"Temperature: {weather_data['main']['temp']}")
   print(f"Feels Like: {weather_data['main']['feels_like']}")
   print(f"Humidity: {weather_data['main']['humidity']}")
   print(f"Weather Report: {weather_data['weather'][0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")


