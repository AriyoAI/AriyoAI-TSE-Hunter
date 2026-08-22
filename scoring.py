def calculate_market_score(stock):

    score = 0
    reasons = []


    # =========================
    # حجم معاملات
    # =========================

    volume_ratio = stock.get(
        "volume_ratio",
        0
    )

    if volume_ratio >= 5:

        score += 30

        reasons.append(
            "حجم معاملات بسیار غیرعادی"
        )

    elif volume_ratio >= 3:

        score += 20

        reasons.append(
            "حجم معاملات غیرعادی"
        )


    # =========================
    # قدرت خریدار
    # =========================

    buyer_power = stock.get(
        "buyer_power",
        0
    )

    if buyer_power >= 3:

        score += 25

        reasons.append(
            "قدرت خریدار بسیار قوی"
        )

    elif buyer_power >= 2:

        score += 15

        reasons.append(
            "قدرت خریدار مناسب"
        )


    # =========================
    # ورود پول حقیقی
    # =========================

    real_money = stock.get(
        "real_money",
        0
    )


    if real_money > 0:

        score += 20

        reasons.append(
            "ورود پول حقیقی"
        )


    # =========================
    # روند
    # =========================

    if stock.get(
        "trend",
        False
    ):

        score += 15

        reasons.append(
            "روند مثبت"
        )


    # =========================
    # شکست مقاومت
    # =========================

    if stock.get(
        "breakout",
        False
    ):

        score += 10

        reasons.append(
            "شکست مقاومت"
        )


    # محدود کردن امتیاز
    if score > 100:

        score = 100


    return {

        "score": score,

        "reasons": reasons

    }
