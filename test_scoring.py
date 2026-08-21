from scoring import calculate_market_score



def test_strong_stock():

    stock = {

        "volume_ratio": 5,

        "buyer_power": 4,

        "real_money": 3,

        "trend": True,

        "breakout": True

    }


    result = calculate_market_score(
        stock
    )


    assert result["score"] == 100



def test_weak_stock():

    stock = {

        "volume_ratio": 1,

        "buyer_power": 1,

        "real_money": 0,

        "trend": False,

        "breakout": False

    }


    result = calculate_market_score(
        stock
    )


    assert result["score"] == 0
