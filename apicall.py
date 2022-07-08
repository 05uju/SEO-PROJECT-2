import requests
import datetime



url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

city = input('Enter your city: ')
offset = input('How many days from today do you want the forecast for?: ')
date = datetime.date.today() + datetime.timedelta(days=int(offset))

querystring = {"q":city,"days":offset,"dt":date}

headers = {
	"X-RapidAPI-Key": "09d4e9e5cfmsh53cd4e0fd2d327ep1ec662jsnda2c540f8b14",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
response = response.json()


