<<<<<<< HEAD
const axios = require("axios");

const options = {
  method: 'GET',
  url: 'https://weatherapi-com.p.rapidapi.com/future.json',
  params: {q: 'London', dt: '2022-12-25'},
  headers: {
    'X-RapidAPI-Key': '105e6a164fmsh8e6337c2093fff8p1eb8a2jsna35061fbf491',
    'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com'
  }
};

axios.request(options).then(function (response) {
	console.log(response.data);
}).catch(function (error) {
	console.error(error);
});
=======
import requests

def currentWeather():
    # This returns up to date current weather information
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":"Providence"}

    headers = {
        "X-RapidAPI-Key": "09d4e9e5cfmsh53cd4e0fd2d327ep1ec662jsnda2c540f8b14",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    
>>>>>>> e881235bfe98058a1f7403b5041cca9ad61ce5c3
