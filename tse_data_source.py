from datetime import datetime


def get_tse_data():

    """
    لایه دریافت داده بورس ایران

    آماده برای اتصال به منبع واقعی TSE
    """

    data = [

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


    return data
