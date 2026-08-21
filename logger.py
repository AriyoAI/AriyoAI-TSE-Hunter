import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)


def log_info(message):

    print(f"[INFO] {message}")
    logging.info(message)



def log_error(message):

    print(f"[ERROR] {message}")
    logging.error(message)
