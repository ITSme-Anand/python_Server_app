#app.py
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello_world():
    return "Hello,World"

@app.get('/weatherReport')
def tell_the_whether():
    return 'veyyil vandha mazha daa...'


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)