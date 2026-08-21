# قوانین اولیه شکار AriyoAI TSE Hunter


STRATEGY = {

    # حداقل امتیاز برای هشدار
    "min_score": 75,

    # حجم غیرعادی نسبت به میانگین
    "min_volume_ratio": 3,

    # حداقل قدرت خریدار
    "min_buyer_power": 2,

    # نیاز به ورود پول حقیقی
    "need_real_money": True,

    # نیاز به روند مثبت
    "need_positive_trend": True
}



def get_strategy():

    return STRATEGY
