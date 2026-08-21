import requests

from datetime import datetime

from logger import (
    log_info,
    log_error
)



FALLBACK_URL = (
    "http://old.tsetmc.com/"
    "tsev2/data/MarketWatchInit.aspx?h=0&r=0"
)



def get_fallback_data():

    try:

        headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64)"
            )
        }


        response = requests.get(
            FALLBACK_URL,
            headers=headers,
            timeout=20
        )


        response.raise_for_status()


        raw = response.text


        parts = raw.split("@")

        if len(parts) < 3:

            log_error(
                "Fallback response invalid"
            )

            return []


        price_rows = parts[2]


        stocks = []


        for row in price_rows.split(";"):

            fields = row.split(",")


            if len(fields) < 14:
                continue


            stocks.append({

                "symbol": fields[2],

                "price": fields[7],

                "volume_ratio": 1,

                "buyer_power": 1,

                "real_money": 0,

                "trend": False,

                "breakout": False,

                "time": datetime.now().isoformat()

            })


        log_info(
            f"Fallback TSE symbols loaded: {len(stocks)}"
        )


        return stocks


    except Exception as error:

        log_error(
            f"Fallback failed: {error}"
        )

        return []
