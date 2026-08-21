from datetime import datetime


def get_market_data():

    """
    لایه دریافت داده بازار

    فعلاً داده آزمایشی است.
    در مرحله بعد به منبع واقعی بازار وصل می‌شود.
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


if __name__ == "__main__":

    data = get_market_data()

    for item in data:
        print(item)
