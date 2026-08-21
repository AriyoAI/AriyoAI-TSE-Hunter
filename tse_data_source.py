import requests

from datetime import datetime

from config import USE_MOCK_DATA

from logger import (
    log_info,
    log_error
)


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


def get_real_data():

    """
    اتصال منبع واقعی بورس ایران

    محل تبدیل داده خام به استاندارد AriyoAI
    """

    try:

        # آدرس منبع واقعی پس از تست نهایی اینجا قرار می‌گیرد

        url = None


        if url is None:

            log_error(
                "Real market source is not configured"
            )

            return []


        response = requests.get(
            url,
            timeout=10
        )


        response.raise_for_status()


        return response.json()


    except Exception as error:

        log_error(
            str(error)
        )

        return []


def get_tse_data():

    try:

        if USE_MOCK_DATA:

            data = get_mock_data()

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
