from analyzer import calculate_score
from bot import send_message


def scan_market():

    # داده آزمایشی
    stock = {
        "symbol": "TEST",
        "volume_ratio": 4,
        "buyer_power": 3,
        "real_money": 2,
        "trend": True,
        "breakout": True
    }

    result = calculate_score(stock)

    if result["signal"]:

        message = f"""
🦅 <b>AriyoAI TSE Hunter</b>

🚨 سیگنال آزمایشی

📌 نماد:
{stock['symbol']}

⭐ امتیاز:
{result['score']}/100

🔎 دلایل:
{', '.join(result['reasons'])}
"""

        send_message(message)


if __name__ == "__main__":
    scan_market()
