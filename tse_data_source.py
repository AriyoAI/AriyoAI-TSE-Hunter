import requests

from datetime import datetime

from logger import (
    log_info,
    log_error
)


TSE_URL = (
    "https://cdn.tsetmc.com/api/"
    "ClosingPrice/GetMarketWatch"
    "?market=0"
    "&paperTypes[0]=1"
    "&paperTypes[1]=2"
    "&paperTypes[2]=3"
    "&withBestLimits=false"
    "&hEven=0"
    "&RefID=0"
)



def get_real_data():

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64)"
        ),
        "Accept": "application/json"
    }


    for attempt in range(1, 4):

        try:

            log_info(
                f"TSE request attempt: {attempt}"
            )


            response = requests.get(
                TSE_URL,
                headers=headers,
                timeout=(5, 20)
            )


            response.raise_for_status()


            raw = response.json()


            market = (
                raw.get("marketwatch")
                or raw.get("marketWatch")
                or []
            )


            stocks = []


            for item in market:

                symbol = item.get(
                    "lVal18AFC",
                    ""
                )


                if not symbol:
                    continue


                stocks.append({

                    "symbol": symbol,

                    "price": item.get(
                        "pDrCotVal",
                        0
                    ),

                    "volume_ratio": 1,

                    "buyer_power": 1,

                    "real_money": 0,

                    "trend": False,

                    "breakout": False,

                    "time": datetime.now().isoformat()

                })


            log_info(
                f"Real TSE symbols loaded: {len(stocks)}"
            )


            return stocks


        except Exception as error:

            log_error(
                f"TSE attempt {attempt} failed: {error}"
            )



    log_error(
        "TSE source unavailable after retries"
    )


    return []



def get_tse_data():

    return get_real_data()
