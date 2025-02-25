# National Weather Service Microservice Communication Contract
This is a microservice that retrieves weather data for Corvallis, OR from the National Weather Service website. This services provides a REST API endpoint that returns temperature and weather description for current date or 14 periods out. 

## How to request data
The selected period needs to be an integer from 0 to 14. 0 represents current period, 1 represents the following period, etc. 

For example: 
If the current period is Monday night then the selected period will be the following: 0 = Monday Night, 1 = Tuesday, 2 = Tuesday Night, 3 = Wednesday, 4 = Wednesday Night, etc.

To request weather data, send a GET request with the selected period to: 
```
http://127.0.0.1:8000/weather/?period={period}
```

Example of Python code to make a request for period 0

```
import requests
response = requests.get("http://127.0.0.1:8000/weather/?period=0")
```

## How to Receive Data
The service returns data in a JSON structure. 
{'period': 'Tonight', 'temperature': '43°F', 'description': 'Showers And Thunderstorms'}
{'period': 'Wednesday', 'temperature': '58°F', 'description': 'Mostly Sunny'}

Python example on how to receive the data: 
```
    if response.status_code == 200:
        return response.json()
```
