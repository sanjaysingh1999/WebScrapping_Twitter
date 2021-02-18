##We will get data from OpenWeather API
import requests, json

api_key = "220337f18a8eb69162f1218ff80e55f0"
base_url = "https://api.openweathermap.org/data/2.5/weather"
payload = {
	"q":"mumbai",
	"appid": api_key
}

response = requests.get(base_url,params=payload)

#my_dict = json.loads(response.text)

my_dict = response.json()

print(my_dict["weather"][0]["description"])
