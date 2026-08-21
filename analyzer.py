from scoring import calculate_market_score
from strategy import get_strategy



def calculate_score(stock):

    strategy = get_strategy()


    result = calculate_market_score(
        stock
    )


    score = result["score"]

    reasons = result["reasons"]


    return {

        "score": score,

        "reasons": reasons,

        "signal": score >= strategy["min_score"]

    }
