import requests

from datetime import datetime

from logger import (
    log_info,
    log_error
)


def get_tse_data():

    """
    لایه دریافت داده بورس ایران

    این نسخه آماده اتصال به منبع عمومی است.
    خروجی استاندارد به سیستم تحلیل می‌دهد.
    """

    try:

        # فعلاً محل اتصال منبع داده عمومی
        # بعد از انتخاب API واقعی این بخش تکمیل می‌شود

        data = []


        log_info(
            f"TSE data received: {len(data)} symbols"
        )


        return data


    except Exception as error:

        log_error(
            str(error)
        )

        return []
