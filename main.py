from scanner import scan_market
from database import create_database
from logger import log_info, log_error


def run():

    try:

        log_info(
            "AriyoAI TSE Hunter started"
        )

        create_database()

        scan_market()

        log_info(
            "AriyoAI TSE Hunter finished successfully"
        )


    except Exception as error:

        log_error(
            str(error)
        )



if __name__ == "__main__":

    run()
