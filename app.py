import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/weather/<city>')
def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    weather_data = response.json()


    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']

    return render_template('weather.html', city=city, temperature=temp, description=description)


@app.route('/weather')
def get_weather_search():

    city = request.args.get('city', '').strip()

    if not city:
        return_to_homepage = render_template('homepage.html', error="Please enter a city name.", city=city)
        return return_to_homepage









    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
                msg = response.json().get('message', 'Unable to fetch weather for that city.')
                return render_template('homepage.html', error=msg.capitalize(), city=city)
        weather_data = response.json()
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

    except requests.exceptions.RequestException:
        return render_template('homepage.html', error='Network error. Please try again', city=city)
    except (KeyError, IndexError, TypeError, ValueError):
        return render_template('homepage.html', error='Unexpected response. Try another city.', city=city)

    return render_template('weather.html', city=city, temperature=temp, description=description)


@app.route('/forecast/<city>')
def get_forecast(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(forecast_url)
    weather_data = response.json()

    # print(weather_data['list'])

    forecasts = []

    for i in range(0, min(40, len(weather_data['list'])), 8):
        forecast = weather_data['list'][0]
        forecasts.append({
            'temp': forecast['main']['temp'],
            'description': forecast['weather'][0]['description'],
            'date': forecast['dt_txt']
        })

    return render_template('forecast.html', city=city, forecasts=forecasts)

if __name__ == '__main__':
    app.run(debug=True, port=3000)