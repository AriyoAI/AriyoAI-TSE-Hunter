import os
import requests

from report_sender import build_report_message



BOT_TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN"
)

CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID"
)



def send_message(message):

    if not BOT_TOKEN or not CHAT_ID:

        raise Exception(
            "Telegram configuration missing"
        )


    url = (
        f"https://api.telegram.org/"
        f"bot{BOT_TOKEN}/sendMessage"
    )


    payload = {

        "chat_id": CHAT_ID,

        "text": message,

        "parse_mode": "HTML"

    }


    response = requests.post(
        url,
        json=payload,
        timeout=10
    )


    response.raise_for_status()



def send_report():

    message = build_report_message()

    send_message(message)
