from analyzer import calculate_score
from bot import send_message
from datetime import datetime


def format_signal(stock, result):

    reasons = "\n".join(
        f"✅ {r}"
        for r in result["reasons"]
    )

    return f"""
🦅 <b>AriyoAI TSE Hunter</b>

🚨 <b>فرصت تحلیلی پیدا شد</b>

📌 نماد:
<b>{stock['symbol']}</b>

⭐ امتیاز:
<b>{result['score']}/100</b>

🔎 دلایل:
{reasons}

⏰ زمان:
{datetime.now().strftime("%Y-%m-%d %H:%M")}

⚠️ هشدار تحلیلی است، نه تضمین سود.
"""


def scan_market():

    # فعلاً داده تستی
    # بعداً با داده واقعی بورس جایگزین می‌شود

    stocks = [
        {
            "symbol": "TEST",
            "volume_ratio": 5,
            "buyer_power": 4,
            "real_money": 3,
            "trend": True,
            "breakout": True
        }
    ]


    for stock in stocks:

        result = calculate_score(stock)

        if result["signal"]:

            message = format_signal(
                stock,
                result
            )

            send_message(message)


if __name__ == "__main__":
    scan_market()
