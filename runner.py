import time

from main import run

from logger import log_error



def start():

    while True:

        try:

            run()


        except Exception as error:

            log_error(
                str(error)
            )


        time.sleep(60)



if __name__ == "__main__":

    start()
