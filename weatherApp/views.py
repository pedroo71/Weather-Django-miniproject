from django.shortcuts import render
import requests
import datetime as dt


#get the name of the city and process the information
def process_input(request):
    if request.method == 'POST':
        input_data = request.POST.get('input_data')
        # Process the input_data
        if input_data:
           context = weather_view(input_data)
           return render(request, 'index.html', context)
        else:
            return render(request, 'index.html')


def weather_view(city):
    api_key = open("C:\\Users\\pedrooli\\OneDrive - Capgemini\\Documents\\GitHub\\Weather\\weatherproject\\API_KEY", "r").read()
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}
    response = requests.get(base_url, params=params)
    data = response.json()

    temp_celsius = kelvin_to_celsius(data['main']['temp'])
    temp_min_celsius = kelvin_to_celsius(data['main']['temp_min'])
    temp_max_celsius = kelvin_to_celsius(data['main']['temp_max'])
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone']) 
    wind_speed = data['wind']['speed']

    context = {
        'city': city.upper(),
        'temp_celsius': temp_celsius,
        'temp_min_celsius': temp_min_celsius,
        'temp_max_celsius': temp_max_celsius,
        'humidity': humidity,
        'description': description.upper(),
        'sunrise_time': sunrise_time,
        'sunset_time': sunset_time,
        'wind_speed': wind_speed
    }

    return context


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius)