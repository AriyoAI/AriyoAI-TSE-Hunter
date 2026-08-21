def is_quality_signal(stock, result):

    """
    فیلتر نهایی کیفیت سیگنال
    """

    # امتیاز پایین رد شود
    if result["score"] < 75:
        return False


    # حجم خیلی کم رد شود
    if stock.get("volume_ratio", 0) < 3:
        return False


    # قدرت خریدار ضعیف رد شود
    if stock.get("buyer_power", 0) < 2:
        return False


    return True
