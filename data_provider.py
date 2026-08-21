from market_data import get_market_data


class MarketProvider:


    def fetch(self):

        data = get_market_data()

        return data
