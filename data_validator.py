def validate_data(data):

    if not data:

        return False


    required = [

        "symbol",

        "price",

        "volume_ratio",

        "buyer_power",

        "real_money",

        "trend",

        "breakout",

        "time"
    ]


    for item in data:

        for field in required:

            if field not in item:

                return False


        if not isinstance(item["symbol"], str):

            return False


        if item["price"] <= 0:

            return False


    return True
