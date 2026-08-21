import os

from database import get_connection



def check_database():

    try:

        conn = get_connection()

        conn.close()

        return True


    except Exception:

        return False



def check_telegram():

    return bool(

        os.getenv(
            "TELEGRAM_BOT_TOKEN"
        )

        and

        os.getenv(
            "TELEGRAM_CHAT_ID"
        )

    )



def system_health():

    return {

        "database":

            check_database(),


        "telegram":

            check_telegram()

    }
