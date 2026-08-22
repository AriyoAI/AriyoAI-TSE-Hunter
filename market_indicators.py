from logger import log_info


def calculate_volume_ratio(stock):

    volume = stock.get(
        "volume",
        0
    )

    avg_volume = stock.get(
        "avg_volume",
        1
    )


    if avg_volume == 0:
        return 0


    return round(
        volume / avg_volume,
        2
    )



def calculate_buyer_power(stock):

    buy = stock.get(
        "buy_volume",
        0
    )

    sell = stock.get(
        "sell_volume",
        1
    )


    if sell == 0:
        return 0


    return round(
        buy / sell,
        2
    )



def calculate_real_money(stock):

    buy_value = stock.get(
        "real_buy",
        0
    )

    sell_value = stock.get(
        "real_sell",
        0
    )


    return (
        buy_value - sell_value
    )



def calculate_trend(stock):

    price = stock.get(
        "price",
        0
    )

    previous = stock.get(
        "previous_price",
        0
    )


    return price > previous



def calculate_indicators(stock):

    result = {

        "volume_ratio":
            calculate_volume_ratio(stock),

        "buyer_power":
            calculate_buyer_power(stock),

        "real_money":
            calculate_real_money(stock),

        "trend":
            calculate_trend(stock)

    }


    log_info(
        f"Indicators calculated: {stock.get('symbol')}"
    )


    return result
