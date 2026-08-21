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

from health_check import system_health

from alert import send_error_alert

from telegram_listener import process_updates



def run():

    try:

        log_info(
            "AriyoAI Hunter started"
        )


        health = system_health()


        if not all(health.values()):

            error = f"System health failed: {health}"

            log_error(error)

            send_error_alert(error)

            return


        process_updates()


        if not is_market_open():

    log_info(
        "Market closed - running test scan mode"
    )
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
            "Report sent successfully"
        )


    except Exception as error:


        add_error()


        log_error(
            str(error)
        )


        send_error_alert(
            str(error)
        )



if __name__ == "__main__":

    run()
