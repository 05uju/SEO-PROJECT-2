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