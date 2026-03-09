import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")

def generate_post(coin):

    post = f"""
Guys! ${coin} created another bullish movement

People lie but chart don’t

#{coin} going to more down in near future

— Follow for more real updates —
"""

    return post


def post_telegram(message):

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    requests.post(url, data=payload)


def post_binance(message):

    url = "https://api.binance.com/bapi/composite/v1/public/square/post"

    headers = {
        "X-MBX-APIKEY": BINANCE_API_KEY
    }

    payload = {
        "content": message
    }

    requests.post(url, json=payload, headers=headers)


def publish(coin):

    post = generate_post(coin)

    post_telegram(post)
    post_binance(post)

    return post
