from analyzer import calculate_score
from bot import send_message
from database import (
    create_database,
    save_signal,
    signal_exists
)

from datetime import datetime


def format_signal(stock, result):

    reasons = "\n".join(
        f"✅ {item}"
        for item in result["reasons"]
    )

    return f"""
🦅 <b>AriyoAI TSE Hunter</b>

🚨 <b>فرصت تحلیلی جدید</b>

📌 نماد:
<b>{stock['symbol']}</b>

⭐ امتیاز:
<b>{result['score']}/100</b>

🔎 دلایل:
{reasons}

⏰ زمان:
{datetime.now().strftime("%Y-%m-%d %H:%M")}

⚠️ این پیام تحلیل داده‌های بازار است، نه تضمین سود.
"""


def get_test_market():

    # فعلاً داده آزمایشی
    # مرحله بعد با داده واقعی بورس جایگزین می‌شود

    return [
        {
            "symbol": "TEST",
            "volume_ratio": 5,
            "buyer_power": 4,
            "real_money": 3,
            "trend": True,
            "breakout": True
        }
    ]


def scan_market():

    stocks = get_test_market()

    for stock in stocks:

        result = calculate_score(stock)

        if result["signal"]:

            symbol = stock["symbol"]

            # جلوگیری از پیام تکراری
            if signal_exists(symbol):
                continue


            message = format_signal(
                stock,
                result
            )


            send_message(message)


            save_signal(
                symbol,
                result["score"],
                result["reasons"]
            )


def main():

    create_database()

    scan_market()


if __name__ == "__main__":
    main()
