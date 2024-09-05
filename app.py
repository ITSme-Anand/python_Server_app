#app.py
from fastapi import FastAPI
import requests

app = FastAPI()
api_key = '196107f35a838a648a4fc4dbbde0868e'

@app.get('/')
def hello_world():
    return "Hello,World"

@app.get('/weatherReport')
def tell_the_whether():
    city = 'coimbatore'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f'Temperature: {temp} K')
        print(f'Description: {desc}')
        return f'temperature:{temp} and description:{desc}'
    else:
        print('Error fetching weather data')
        return 'error'
    



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)