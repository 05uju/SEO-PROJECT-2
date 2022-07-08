import requests
import datetime
import json
import pprint
import sqlalchemy as db
import pandas as pd
#from sqlalchemy import create_engine

# Create a dataframe to hold the api data
col_names = ['City', 'Temperature', 'Dates']
df = pd.DataFrame(columns= col_names)

# Get the user input
city = input('Enter your city: ')
offset = input('How many days in advance do you want the weather for?: ')
date = datetime.date.today() + datetime.timedelta(days=int(offset))
temperature = ''
dates = ''

# Define the input needed for the API call
url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
querystring = {"q":city,"days":offset,"dt":date}
headers = {
	"X-RapidAPI-Key": "09d4e9e5cfmsh53cd4e0fd2d327ep1ec662jsnda2c540f8b14",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

# Convert the API data to a python dictionary
response = requests.request("GET", url, headers=headers, params=querystring)
dict_data = json.loads(response.text)
pprint.pprint(dict_data)

# df.loc[len(df.index)] = [city, dict_data['forecast']['forecastday'][0]['date'], temperature, ['forecast']['forecastday'][0]['day']['avgtemp_f'], dates,['forecast']['forecastday'][0]['day']['avgtemp_f']]

# print(df)
# pprint.pprint(dict_data)


# Filter the dictionary data to move selected

# engine = db.create_engine('sqlite:///weather_data.db')

# # query_result = engine.execute("SELECT * FROM table;").fetchall()
# # print(pd.DataFrame(query_result))

# query_result = engine.execute("SELECT * FROM weather;").fetchall()

# print(query_result)
