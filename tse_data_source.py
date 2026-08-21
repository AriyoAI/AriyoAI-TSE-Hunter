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
    محل اتصال منبع واقعی بورس ایران

    بعد از انتخاب API واقعی تکمیل می‌شود.
    """

    return []



def get_tse_data():

    try:

        if USE_MOCK_DATA:

            data = get_mock_data()

            log_info(
                "Using mock TSE data"
            )

        else:

            data = get_real_data()


        log_info(
            f"TSE data received: {len(data)} symbols"
        )


        return data


    except Exception as error:

        log_error(
            str(error)
        )

        return []
