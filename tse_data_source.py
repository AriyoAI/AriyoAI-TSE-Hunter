import requests

from datetime import datetime

from logger import (
    log_info,
    log_error
)

from tse_fallback_source import get_fallback_data

from demo_data_source import get_demo_data



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



def get_primary_data():

    try:

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        }


        response = requests.get(
            TSE_URL,
            headers=headers,
            timeout=(5, 15)
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
            f"Primary TSE symbols loaded: {len(stocks)}"
        )


        return stocks


    except Exception as error:

        log_error(
            f"Primary TSE failed: {error}"
        )

        return []



def get_real_data():

    data = get_primary_data()


    if data:

        return data



    log_info(
        "Switching to TSE fallback source"
    )


    data = get_fallback_data()


    if data:

        return data



    log_info(
        "Switching to Demo Provider"
    )


    return get_demo_data()



def get_tse_data():

    return get_real_data()
