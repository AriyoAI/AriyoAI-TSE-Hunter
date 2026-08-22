from market_data import get_market_data
from data_validator import validate_data

from logger import (
    log_info,
    log_error
)



class MarketProvider:


    def fetch(self):

        try:

            log_info(
                "Fetching market data..."
            )


            data = get_market_data()


            if not data:

                log_error(
                    "No market data received"
                )

                return []


            if not validate_data(data):

                log_error(
                    "Invalid market data structure"
                )

                return []


            log_info(
                f"Market data validated: {len(data)} symbols"
            )


            return data



        except Exception as error:

            log_error(
                f"MarketProvider error: {error}"
            )

            return []
