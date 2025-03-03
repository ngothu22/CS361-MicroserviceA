import requests

def request_weather_data(period):
    url = f"http://127.0.0.1:8000/weather/?period={period}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return


# query up to 14 periods, use 0 for current period
period = 0
corvallis_weather = request_weather_data(period)
print(corvallis_weather)

period = 3
corvallis_weather = request_weather_data(period)
print(corvallis_weather)

