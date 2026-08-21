from datetime import datetime


def get_market_data():

    """
    دریافت داده بازار

    فعلاً حالت آزمایشی.
    در مرحله بعد به منبع واقعی وصل می‌شود.
    """

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



def validate_market_data(data):

    required_fields = [
        "symbol",
        "price",
        "volume_ratio",
        "buyer_power"
    ]

    for item in data:

        for field in required_fields:

            if field not in item:
                return False

    return True
