import requests

from datetime import datetime

from logger import (
    log_info,
    log_error
)



def source_tse():

    """
    منبع اصلی TSE
    """

    url = (
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


    try:

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=8
        )


        response.raise_for_status()


        data = response.json()


        market = data.get(
            "marketwatch",
            []
        )


        stocks = []


        for item in market:

            symbol = item.get(
                "lVal18AFC",
                ""
            )


            if symbol:

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


        if stocks:

            log_info(
                f"Source1 TSE loaded: {len(stocks)}"
            )

            return stocks


    except Exception as error:

        log_error(
            f"Source1 failed: {error}"
        )


    return []





def source_backup():

    """
    منبع جایگزین
    فعلاً آماده اتصال API دوم
    """

    log_info(
        "Backup source unavailable"
    )

    return []





def get_market_sources():


    sources = [

        source_tse,

        source_backup

    ]


    for source in sources:

        data = source()


        if data:

            return data



    return []
