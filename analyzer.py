from strategy import get_strategy


def calculate_score(stock):

    strategy = get_strategy()

    score = 0
    reasons = []


    # حجم غیرعادی
    if stock.get("volume_ratio", 0) >= strategy["min_volume_ratio"]:

        score += 25
        reasons.append("حجم غیرعادی")


    # قدرت خریدار
    if stock.get("buyer_power", 0) >= strategy["min_buyer_power"]:

        score += 20
        reasons.append("قدرت خریدار مناسب")


    # پول حقیقی
    if strategy["need_real_money"]:

        if stock.get("real_money", 0) > 0:

            score += 20
            reasons.append("ورود پول حقیقی")


    # روند مثبت
    if strategy["need_positive_trend"]:

        if stock.get("trend", False):

            score += 20
            reasons.append("روند مثبت")


    # شکست مقاومت
    if stock.get("breakout", False):

        score += 15
        reasons.append("شکست مقاومت")


    return {

        "score": score,

        "reasons": reasons,

        "signal": score >= strategy["min_score"]

    }
