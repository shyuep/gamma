import os
import requests
from datetime import datetime
import pandas as pd


class AlphaVantage:

    url = "https://www.alphavantage.co/query"

    def __init__(self, api_key=None):
        """
        :param api_key: API key for AlphaVantage. Get it from
            https://www.alphavantage.co/support/#api-key
        """
        self.api_key = api_key if api_key is not None \
            else os.environ["ALPHA_VANTAGE_APIKEY"]
        self.session = requests.Session()

    def get_daily_data(self, symbol, fmt="df", **kwargs):
        """
        :param symbol:
        :param fmt:
        :param kwargs: These are passthrough as additional keywords to control
            the output. E.g., outputsize="full" provides 20 year data rather
            than just 100 data points.
        :return:
        """
        payload = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.api_key
        }
        payload.update(kwargs)

        response = self.session.get(self.url, params=payload)

        if response.status_code in [200, 400]:
            raw = response.json()
            if fmt == "json":
                return raw

            # Format of time series string as of 2017-10-19.
            # {'2017-10-19': {'1. open': '234.0300', '2. high': '234.9900',
            # '3. low': '233.6200', '4. close': '234.9900',
            # '5. volume': '1653619'}
            index = []
            data = []
            columns = []
            for k, v in raw['Time Series (Daily)'].items():
                date = datetime.strptime(k, "%Y-%m-%d")
                index.append(date)
                row = [float(v[k2]) for k2 in sorted(v.keys())]
                columns = [s.split(".")[-1].strip() for s in sorted(v.keys())]
                data.append(row)
            return pd.DataFrame(data, index=index, columns=columns)

        raise ValueError("REST query returned with error status code {}"
                         .format(response.status_code))


import unittest


class AlphaVantageTest(unittest.TestCase):

    def test_get_daily_data(self):
        source = AlphaVantage()
        df = source.get_daily_data("VOO")
        self.assertEqual(len(df), 100)


if __name__ == "__main__":
    unittest.main()
