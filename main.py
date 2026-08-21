from scanner import scan_market

from database import create_database

from logger import (
    log_info,
    log_error
)

from market_time import is_market_open



def run():

    try:

        log_info(
            "AriyoAI Hunter started"
        )


        if not is_market_open():

            log_info(
                "Market is closed. Scan skipped."
            )

            return


        create_database()

        scan_market()


        log_info(
            "Hunter finished successfully"
        )


    except Exception as error:

        log_error(
            str(error)
        )



if __name__ == "__main__":

    run()
