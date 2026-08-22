from datetime import datetime

from logger import (
    log_info,
    log_error
)

from market_sources import get_market_sources



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
        }

    ]


    log_info(
        f"Demo symbols loaded: {len(data)}"
    )


    return data





def get_tse_data():

    try:

        log_info(
            "Requesting market sources..."
        )


        data = get_market_sources()


        if data:

            log_info(
                f"Market source selected: {len(data)} symbols"
            )

            return data



        log_error(
            "All market sources failed"
        )


    except Exception as error:

        log_error(
            f"TSE data source error: {error}"
        )



    log_info(
        "Switching to Demo Provider"
    )


    return get_demo_data()
