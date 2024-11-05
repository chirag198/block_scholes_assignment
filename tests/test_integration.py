import unittest
from market_data.market_data_fetcher import MarketDataFetcher


class IntegrationTest(unittest.TestCase):
    def test_integration_fetch_data(self):
        fetcher = MarketDataFetcher()
        prices = fetcher.fetch_daily_closing_prices("2024-07-01", "2024-07-31")

        self.assertGreater(len(prices), 0)
        for price in prices:
            self.assertIsNotNone(price.date)
            self.assertIsNotNone(price.closing_price)
