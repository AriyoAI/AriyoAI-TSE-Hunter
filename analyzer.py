from config import (
    MIN_SCORE,
    VOLUME_MULTIPLIER,
    MIN_BUYER_POWER
)


def calculate_score(stock):
    """
    محاسبه امتیاز سهم از 100
    """

    score = 0
    reasons = []

    # حجم غیرعادی
    volume_ratio = stock.get("volume_ratio", 0)

    if volume_ratio >= VOLUME_MULTIPLIER:
        score += 25
        reasons.append("حجم غیرعادی")


    # قدرت خریدار
    buyer_power = stock.get("buyer_power", 0)

    if buyer_power >= MIN_BUYER_POWER:
        score += 20
        reasons.append("قدرت خریدار مناسب")


    # ورود پول حقیقی
    real_money = stock.get("real_money", 0)

    if real_money > 0:
        score += 20
        reasons.append("ورود پول حقیقی")


    # روند قیمت
    trend = stock.get("trend", False)

    if trend:
        score += 20
        reasons.append("روند صعودی")


    # شکست مقاومت
    breakout = stock.get("breakout", False)

    if breakout:
        score += 15
        reasons.append("شکست مقاومت")


    return {
        "score": score,
        "reasons": reasons,
        "signal": score >= MIN_SCORE
  }
