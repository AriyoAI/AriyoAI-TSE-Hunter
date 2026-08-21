import requests

from datetime import datetime

from config import USE_MOCK_DATA

from logger import (
    log_info,
    log_error
)


# ---------------------------------
# Mock Data (Test Mode)
# ---------------------------------

def get_mock_data():

    return [
        {
            "symbol": "TEST",
            "price": 1000,
            "volume_ratio": 5,
            "buyer_power": 4,
            "real_money": 3,
            "trend": True,
            "breakout": True,
            "time": datetime.now().isoformat()
        }
    ]


# ---------------------------------
# Real Data Connection
# ---------------------------------

def get_real_data():

    """
    محل اتصال داده واقعی بورس ایران

    خروجی استاندارد AriyoAI:
    symbol
    price
    volume_ratio
    buyer_power
    real_money
    trend
    breakout
    time
    """

    try:

        # این آدرس بعد از انتخاب endpoint نهایی تکمیل می‌شود
        url = ""

        if not url:

            log_info(
                "Real data source not configured yet"
            )

            return []


        response = requests.get(
            url,
            timeout=10
        )


        response.raise_for_status()


        raw_data = response.json()


        stocks = []


        for item in raw_data:

            stocks.append({

                "symbol": item.get("symbol"),

                "price": item.get(
                    "price",
                    0
                ),

                "volume_ratio": item.get(
                    "volume_ratio",
                    0
                ),

                "buyer_power": item.get(
                    "buyer_power",
                    0
                ),

                "real_money": item.get(
                    "real_money",
                    0
                ),

                "trend": item.get(
                    "trend",
                    False
                ),

                "breakout": item.get(
                    "breakout",
                    False
                ),

                "time": datetime.now().isoformat()

            })


        return stocks


    except Exception as error:

        log_error(
            str(error)
        )

        return []


# ---------------------------------
# Main Provider
# ---------------------------------

def get_tse_data():

    try:

        if USE_MOCK_DATA:

            data = get_mock_data()

            log_info(
                "Using mock data"
            )

        else:

            data = get_real_data()


        log_info(
            f"TSE symbols loaded: {len(data)}"
        )


        return data


    except Exception as error:

        log_error(
            str(error)
        )

        return []
