from logger import log_error



def validate_data(data):

    if not data:

        log_error(
            "Empty market data"
        )

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


    valid_count = 0


    for item in data:


        valid = True


        for field in required:

            if field not in item:

                log_error(
                    f"Missing field {field} in {item}"
                )

                valid = False

                break



        if not valid:

            continue



        if not item["symbol"]:

            continue



        if item["price"] <= 0:

            continue



        if item["volume_ratio"] < 0:

            continue



        if item["buyer_power"] < 0:

            continue



        valid_count += 1



    if valid_count == 0:

        log_error(
            "No valid market symbols found"
        )

        return False



    return True
