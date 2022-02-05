import requests

def weather_data():
    city = "Boston"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=5b7c0160aba9fac1ce81db90f1ed4411&units=metric'.format(city)
    res = requests.get(url)
    data = res.json()

    temp = data['main']['temp'] #temperature 
    wind_speed = data['wind']['speed'] #windspeed
    feels = data['main']['feels_like'] #what the temperature feels like

    message1 = (
        f"Good Morning Rachel."
        f"Today's temperature is {temp} celsius but it feels like {feels} celsius."
        f"Current wind speed is {wind_speed}."
        f"Please dress accordingly."
    )
    return message1

#print(weather_data())