from analyzer import calculate_score
from bot import send_message

from database import (
    create_database,
    save_signal,
    signal_exists
)

from data_provider import MarketProvider

from signal_filter import is_quality_signal

from signal_history import save_history

from report import add_signal

from logger import (
    log_info,
    log_error
)

from datetime import datetime



def format_signal(stock, result):

    reasons = "\n".join(
        f"✅ {item}"
        for item in result["reasons"]
    )

    return f"""
🦅 <b>AriyoAI TSE Hunter</b>

🚨 <b>سیگنال با کیفیت</b>

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

⚠️ هشدار تحلیلی است.
"""



def scan_market():

    provider = MarketProvider()

    stocks = provider.fetch()


    log_info(
        f"Scan started. Symbols: {len(stocks)}"
    )


    for stock in stocks:

        result = calculate_score(stock)


        if not result["signal"]:
            continue


        if not is_quality_signal(stock, result):

            log_info(
                f"Low quality ignored: {stock['symbol']}"
            )

            continue


        symbol = stock["symbol"]


        if signal_exists(symbol):

            log_info(
                f"Duplicate ignored: {symbol}"
            )

            continue


        save_history(
            symbol,
            result["score"]
        )


        message = format_signal(
            stock,
            result
        )


        send_message(message)

        add_signal()


        save_signal(
            symbol,
            result["score"],
            result["reasons"]
        )


        log_info(
            f"Signal sent: {symbol}"
        )



def main():

    try:

        create_database()

        scan_market()


    except Exception as error:

        log_error(
            str(error)
        )



if __name__ == "__main__":

    main()
