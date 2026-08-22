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


def parse_tse_data(raw):

    market = raw.get(
        "marketwatch",
        []
    )

    stocks = []

    for item in market:

        symbol = item.get(
            "lVal18AFC",
            ""
        )

        price = item.get(
            "pDrCotVal",
            0
        )

        previous_price = item.get(
            "pClosing",
            0
        )

        if not symbol or not price:
            continue

        stocks.append({

            "symbol": symbol,

            "price": price,

            "volume": item.get(
                "qTotTran5J",
                0
            ),

            "avg_volume": 1,

            "buy_volume": 1,

            "sell_volume": 1,

            "real_buy": 0,

            "real_sell": 0,

            "previous_price": previous_price,

            "volume_ratio": 1,

            "buyer_power": 1,

            "real_money": 0,

            "trend": (
                price > previous_price
                if previous_price
                else False
            ),

            "breakout": False,

            "time": datetime.now().isoformat()

        })

    return stocks


def source_tse():

    try:

        log_info(
            "Trying Source 1: TSE"
        )

        response = requests.get(
            TSE_URL,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(Windows NT 10.0; Win64; x64)"
                )
            },
            timeout=(5, 8)
        )

        response.raise_for_status()

        raw = response.json()

        stocks = parse_tse_data(raw)

        if stocks:

            log_info(
                f"Source 1 TSE loaded: {len(stocks)} symbols"
            )

            return stocks

        log_error(
            "Source 1 returned no symbols"
        )

    except requests.exceptions.Timeout:

        log_error(
            "Source 1 TSE timeout"
        )

    except Exception as error:

        log_error(
            f"Source 1 TSE failed: {error}"
        )

    return []


def source_backup():

    """
    Source 2 placeholder.

    این لایه عمداً مستقل نگه داشته شده
    تا منبع واقعی جایگزین بدون دستکاری
    Scanner و Analyzer اضافه شود.
    """

    try:

        log_info(
            "Trying Source 2: Backup"
        )

        # منبع واقعی دوم در مرحله بعد
        # اینجا متصل می‌شود.

        return []

    except Exception as error:

        log_error(
            f"Source 2 Backup failed: {error}"
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

    log_error(
        "All real market sources failed"
    )

    return []
