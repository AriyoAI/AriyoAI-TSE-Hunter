from datetime import datetime


def is_market_open():

    now = datetime.now()

    hour = now.hour
    minute = now.minute


    # بازه نمونه بازار
    # بعداً با ساعت دقیق و منطقه زمانی تنظیم می‌شود

    start = (9, 0)
    end = (12, 30)


    current = (
        hour,
        minute
    )


    return start <= current <= end
