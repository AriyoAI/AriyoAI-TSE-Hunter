import requests
from config import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID
)


def send_message(text):
    """
    ارسال پیام به تلگرام
    """

    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        raise ValueError(
            "Telegram settings are missing"
        )

    url = (
        f"https://api.telegram.org/"
        f"bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    )

    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    response = requests.post(
        url,
        data=data,
        timeout=15
    )

    return response.json()


if __name__ == "__main__":

    send_message(
        """
🦅 <b>AriyoAI TSE Hunter</b>

✅ موتور پیام‌رسان فعال شد

آماده دریافت سیگنال‌های تحلیلی هستیم 📊
"""
    )
