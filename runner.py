import time

from main import run

from logger import log_error

from config import SCAN_INTERVAL



def start():

    while True:

        try:

            run()


        except Exception as error:

            log_error(
                str(error)
            )


        time.sleep(
            SCAN_INTERVAL
        )



if __name__ == "__main__":

    start()
