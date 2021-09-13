from random import choice
import requests

keys = [
    '95663f8c16mshb876a3c5807479cp1a88f2jsn759840e75b25',
    'b1f856eda9msh246cbabbce35faap1448b2jsn4d82f04c14e8',
    '0c27999ea5mshfc8e8aa7a1ad4f3p1b2d38jsn99d12abf2011',
    '701af1c007mshb4c6d0a291b3b4fp1fa4a0jsn9d7074b45d8c',
    '3fdd7f0747msh5f8800058098df9p1ee141jsn40c42d3053c5',
    '84e2eb9569mshd12ce921d2a4041p14c24ajsncaf717d18da4',
    'a71c7aa390msh522ca5e399c79cfp19a1f4jsn74ddc6c80b8d',
]

key = 0

urls = {
    'current': 'https://weatherbit-v1-mashape.p.rapidapi.com/current',
    'hourly': 'https://weatherbit-v1-mashape.p.rapidapi.com/forecast/hourly',
    'daily': 'https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily',
    }


def get_forecast(city, forecast_type):
    global key
    url = urls[forecast_type]
    headers = {
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
        'x-rapidapi-key': keys[key]
    }
    response = requests.get(url, headers=headers, params={"city": city})
    key = (key + 1) % len(keys)
    if response.text == '':
        return None
    if 'message' in response.json().keys():
        return get_forecast(city, forecast_type)
    return response.json()['data']
