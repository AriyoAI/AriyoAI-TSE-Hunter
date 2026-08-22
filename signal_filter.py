from strategy import get_strategy



def is_quality_signal(stock, result):

    """
    فیلتر نهایی کیفیت سیگنال AriyoAI
    """

    strategy = get_strategy()


    # حداقل امتیاز
    if result.get("score", 0) < strategy["min_score"]:

        return False


    # حجم معاملات
    if stock.get(
        "volume_ratio",
        0
    ) < strategy["min_volume_ratio"]:

        return False


    # قدرت خریدار
    if stock.get(
        "buyer_power",
        0
    ) < strategy["min_buyer_power"]:

        return False


    # ورود پول حقیقی
    if strategy["need_real_money"]:

        if stock.get(
            "real_money",
            0
        ) <= 0:

            return False


    # روند مثبت
    if strategy["need_positive_trend"]:

        if not stock.get(
            "trend",
            False
        ):

            return False


    # شکست مقاومت (اختیاری)
    if strategy.get(
        "need_breakout",
        False
    ):

        if not stock.get(
            "breakout",
            False
        ):

            return False


    return True
