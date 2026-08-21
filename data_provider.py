from market_data import get_market_data
from data_validator import validate_data

from logger import (
    log_info,
    log_error
)


class MarketProvider:


    def fetch(self):

        try:

            data = get_market_data()


            if not validate_data(data):

                log_error(
                    "Invalid market data"
                )

                return []


            log_info(
                f"Market data validated: {len(data)} symbols"
            )


            return data


        except Exception as error:

            log_error(
                str(error)
            )

            return []
