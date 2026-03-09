from fastapi import FastAPI
from poster import publish

app = FastAPI()


@app.get("/")
def home():
    return {"status": "Bot Running"}


@app.get("/post/{coin}")
def post_coin(coin: str):

    message = publish(coin.upper())

    return {
        "status": "posted",
        "coin": coin,
        "message": message
    }
