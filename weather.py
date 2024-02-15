import requests
from dotenv import load_dotenv #help us to import variable
#By calling load_dotenv(), the values from the .env file will be loaded into the environment, and you can access them using os.getenv().
import os
load_dotenv() #call the variables in the .env file
from pprint import pprint #pretty print to make json boject easier to read in the terminal

def get_current_weather():
    print('\n***Current weather ***\n')

    city = input("\nEnter a city name:\n")

    #os.getenv using vaariable name in env file, we laoded those values from load_dotenv
    request_url=f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"

    # print(request_url)
    weather_data = requests.get(request_url).json()
    # pprint(weather_data) #to print and show json data

    print(f'\nCurrent weather for {weather_data["name"]}\n')
    print(f'\nCurrent Temperature {weather_data["main"]["temp"]}\n')
    print(f'\nPerceived Temperature {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"].capitalize()}\n')

# if __name__ == "__main":

get_current_weather()