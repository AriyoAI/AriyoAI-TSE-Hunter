from analyzer import calculate_score
from bot import send_message

from database import (
    create_database,
    save_signal,
    signal_exists
)

from market_data import get_market_data

from datetime import datetime



def format_signal(stock, result):

    reasons = "\n".join(
        f"✅ {item}"
        for item in result["reasons"]
    )

    return f"""
🦅 <b>AriyoAI TSE Hunter</b>

🚨 <b>سیگنال تحلیلی جدید</b>

📌 نماد:
<b>{stock['symbol']}</b>

💰 قیمت:
{stock.get('price', '-')}

⭐ امتیاز:
<b>{result['score']}/100</b>

🔎 دلایل:
{reasons}

⏰ زمان:
{datetime.now().strftime("%Y-%m-%d %H:%M")}

⚠️ این فقط هشدار تحلیلی است.
"""



def scan_market():

    stocks = get_market_data()

    for stock in stocks:

        result = calculate_score(stock)


        if result["signal"]:

            symbol = stock["symbol"]


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
