import requests
from datetime import date

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

city = input('Enter your city: ')
days = input('How many days in advance do you want the weather for?: ')
today = date.today()

querystring = {"q":city,"days":days,"dt":today}

headers = {
	"X-RapidAPI-Key": "09d4e9e5cfmsh53cd4e0fd2d327ep1ec662jsnda2c540f8b14",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
#print(response.text)

#print(response['current']['temp_f'])

response = requests.request("GET", url, headers=headers, params=querystring)
response = response.json()


