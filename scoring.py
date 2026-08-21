def calculate_market_score(stock):

    score = 0
    reasons = []


    # حجم معاملات
    if stock.get("volume_ratio", 0) >= 3:

        score += 25
        reasons.append(
            "حجم معاملات غیرعادی"
        )


    # قدرت خریدار
    if stock.get("buyer_power", 0) >= 2:

        score += 25
        reasons.append(
            "قدرت خریدار مناسب"
        )


    # ورود پول حقیقی
    if stock.get("real_money", 0) > 0:

        score += 20
        reasons.append(
            "ورود پول حقیقی"
        )


    # روند
    if stock.get("trend", False):

        score += 15
        reasons.append(
            "روند مثبت"
        )


    # شکست مقاومت
    if stock.get("breakout", False):

        score += 15
        reasons.append(
            "شکست مقاومت"
        )


    return {
        "score": score,
        "reasons": reasons
    }
