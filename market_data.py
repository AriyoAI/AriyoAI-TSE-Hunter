from tse_data_source import get_tse_data

from logger import (
    log_info,
    log_error
)



def get_market_data():

    """
    دریافت داده بازار بورس ایران
    داده از لایه TSE Data Source دریافت می‌شود.
    """

    try:

        data = get_tse_data()


        log_info(
            f"Market source returned: {len(data)} symbols"
        )


        return data


    except Exception as error:

        log_error(
            f"Market data error: {error}"
        )

        return []
