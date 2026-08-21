import os
import requests

from telegram_commands import handle_command



BOT_TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN"
)



def get_updates():

    url = (
        f"https://api.telegram.org/"
        f"bot{BOT_TOKEN}/getUpdates"
    )


    response = requests.get(
        url,
        timeout=10
    )


    return response.json()



def process_updates():

    data = get_updates()


    for item in data.get("result", []):

        message = item.get(
            "message",
            {}
        )


        text = message.get(
            "text",
            ""
        )


        if text.startswith("/"):

            handle_command(text)
