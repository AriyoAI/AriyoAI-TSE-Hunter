import os
import requests

from report_sender import build_report_message
from status import get_system_status



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



def send_status():

    status = get_system_status()

    health = status["health"]


    message = f"""
🦅 <b>AriyoAI Status</b>

🗄️ Database:
{"🟢 OK" if health["database"] else "🔴 ERROR"}

📱 Telegram:
{"🟢 OK" if health["telegram"] else "🔴 ERROR"}


🔎 Scans:
{status["scans"]}

🚨 Signals:
{status["signals"]}

📊 Stored Signals:
{status["stored_signals"]}

⭐ Average Score:
{status["average_score"]}
"""


    send_message(message)
