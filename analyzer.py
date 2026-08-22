from scoring import calculate_market_score
from strategy import get_strategy

from logger import log_info



def calculate_score(stock):

    strategy = get_strategy()


    result = calculate_market_score(
        stock
    )


    score = result.get(
        "score",
        0
    )


    reasons = result.get(
        "reasons",
        []
    )


    signal = (
        score >= strategy["min_score"]
    )


    log_info(
        f"Analysis {stock.get('symbol', '-')}: {score}/100"
    )


    return {

        "score": score,

        "reasons": reasons,

        "signal": signal

    }
