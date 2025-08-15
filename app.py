import os
import requests
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)



@app.route('/')
def home():
    return "Weather Dashboard coming soon!"


@app.route('/weather/<city>')
def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    weather_data = response.json()


    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']

    return f"Weather in {city}: {temp} Degrees, {description}"

if __name__ == '__name__':
    app.run(debug=True, port=3000)