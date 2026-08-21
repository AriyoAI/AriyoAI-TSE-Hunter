from scanner import scan_market

from database import create_database

from logger import (
    log_info,
    log_error
)

from market_time import is_market_open

from report import (
    add_scan,
    add_error,
    get_report
)

from bot import send_report



def run():

    try:

        log_info(
            "AriyoAI Hunter started"
        )


        if not is_market_open():

            log_info(
                "Market closed"
            )

            return


        create_database()


        add_scan()


        scan_market()


        report = get_report()


        log_info(
            f"Report: {report}"
        )


        send_report()


        log_info(
            "Report sent to Telegram"
        )


    except Exception as error:

        add_error()


        log_error(
            str(error)
        )



if __name__ == "__main__":

    run()
