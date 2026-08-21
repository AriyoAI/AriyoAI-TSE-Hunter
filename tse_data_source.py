import requests

from datetime import datetime

from logger import (
    log_info,
    log_error
)

from config import DATA_SOURCE



def get_tse_data():

    """
    دریافت داده بورس ایران

    آماده اتصال به منبع واقعی TSE
    """

    try:

        log_info(
            f"Data source: {DATA_SOURCE}"
        )


        # این بخش محل اتصال API واقعی بورس خواهد بود
        # بعد از انتخاب منبع داده تکمیل می‌شود

        data = []


        log_info(
            f"TSE data received: {len(data)} symbols"
        )


        return data


    except requests.exceptions.RequestException as error:

        log_error(
            f"Connection error: {error}"
        )

        return []


    except Exception as error:

        log_error(
            str(error)
        )

        return []
