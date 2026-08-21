def validate_data(data):

    if not data:

        return False


    required = [
        "symbol",
        "price",
        "volume_ratio",
        "buyer_power"
    ]


    for item in data:

        for field in required:

            if field not in item:

                return False


    return True
