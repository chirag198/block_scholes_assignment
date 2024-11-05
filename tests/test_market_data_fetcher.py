import unittest
from unittest.mock import patch
from datetime import datetime
from market_data.market_data_fetcher import MarketDataFetcher


class TestMarketDataFetcher(unittest.TestCase):
    @patch("market_data.market_data_fetcher.requests.get")
    def test_fetch_daily_closing_prices(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "code": "0",
            "msg": "",
            "data": [
                ["1688476800000", "30000", "31000", "29500", "30300", "5000", "1000", "500000", "1"]
            ]
        }

        fetcher = MarketDataFetcher()
        prices = fetcher.fetch_daily_closing_prices("2023-07-04", "2023-07-04")

        expected_date = datetime.utcfromtimestamp(1688476800000 / 1000)

        self.assertEqual(prices[0].date, expected_date)
        self.assertEqual(prices[0].closing_price, 30300.0)
