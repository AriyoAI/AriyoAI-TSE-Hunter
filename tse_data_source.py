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

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }


        response = requests.get(
            TSE_URL,
            headers=headers,
            timeout=(10, 60)
        )


        response.raise_for_status()


        raw = response.json()


        market = raw.get(
            "marketwatch",
            []
        )


        stocks = []


        for item in market:

            stock = {

                "symbol": item.get(
                    "lVal18AFC",
                    ""
                ),

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

            }


            if stock["symbol"]:

                stocks.append(stock)


        log_info(
            f"Real TSE symbols loaded: {len(stocks)}"
        )


        return stocks


    except requests.exceptions.Timeout:

        log_error(
            "TSE data request timed out"
        )

        return []


    except Exception as error:

        log_error(
            str(error)
        )

        return []



def get_tse_data():

    return get_real_data()
