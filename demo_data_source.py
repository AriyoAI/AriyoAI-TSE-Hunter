from datetime import datetime

from logger import log_info


def get_demo_data():

    data = [

        {
            "symbol": "TEST1",
            "price": 1000,
            "volume_ratio": 5,
            "buyer_power": 4,
            "real_money": 3,
            "trend": True,
            "breakout": True,
            "time": datetime.now().isoformat()
        },

        {
            "symbol": "TEST2",
            "price": 2500,
            "volume_ratio": 2,
            "buyer_power": 3,
            "real_money": 1,
            "trend": True,
            "breakout": False,
            "time": datetime.now().isoformat()
        }

    ]


    log_info(
        f"Demo symbols loaded: {len(data)}"
    )


    return data
