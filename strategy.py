# قوانین استراتژی AriyoAI TSE Hunter


STRATEGY = {

    # حداقل امتیاز برای ارسال هشدار
    "min_score": 75,


    # امتیازهای مهم
    "min_volume_ratio": 3,

    "min_buyer_power": 2,


    # فیلترهای تاییدی

    "need_real_money": True,

    "need_positive_trend": True,

    "need_breakout": False,


    # سطح‌بندی سیگنال

    "strong_signal_score": 90,

    "medium_signal_score": 75,


    # کنترل ریسک

    "max_duplicate_signal": 1

}



def get_strategy():

    return STRATEGY
