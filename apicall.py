import requests

# This returns up to date current weather information
url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"Providence"}

headers = {
	"X-RapidAPI-Key": "09d4e9e5cfmsh53cd4e0fd2d327ep1ec662jsnda2c540f8b14",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)