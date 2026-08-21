from tse_data_source import get_tse_data


def get_market_data():
    """
    دریافت داده بازار بورس ایران
    داده از لایه TSE Data Source دریافت می‌شود.
    """

    return get_tse_data()



def validate_market_data(data):

    required_fields = [
        "symbol",
        "price",
        "volume_ratio",
        "buyer_power",
        "real_money",
        "trend",
        "breakout"
    ]


    for item in data:

        for field in required_fields:

            if field not in item:

                return False


    return True
