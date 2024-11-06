import time
from datetime import datetime, timedelta
import requests
from .interfaces import MarketDataInterface
from .price_data import PriceData


class MarketDataFetcher(MarketDataInterface):
    """
    Fetches daily closing prices for a specified date range using the OKX API.

    Attributes:
        BASE_URL (str): The base URL for OKX's market history endpoint.
    """




















    BASE_URL = "https://okx.com/api/v5/market/history-candles"

    def fetch_daily_closing_prices(self, start_date: str, end_date: str) -> list:
        """
        Retrieves daily closing prices from OKX for BTC-USD within the specified date range.

        Args:
            start_date (str): Start date in the format 'YYYY-MM-DD'.
            end_date (str): End date in the format 'YYYY-MM-DD'.

        Returns:
            list: A list of PriceData objects, each containing the date and closing price for that date.
        """
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        results = []
        current_date = start

        while current_date <= end:
            timestamp = int(current_date.timestamp() * 1000)

            params = {
                "instId": "BTC-USD-SWAP",
                "bar": "1D",
                "limit": 1,
                "before": timestamp
            }

            success = False
            retries = 3
            attempt = 0

            while not success and attempt < retries:
                try:
                    response = requests.get(self.BASE_URL, params=params, timeout=10)
                    response.raise_for_status()
                    data = response.json()

                    if data.get("data"):
                        daily_data = data["data"][0]
                        date = datetime.utcfromtimestamp(int(daily_data[0]) / 1000)
                        close_price = float(daily_data[4])

                        price_data = PriceData(date=date, closing_price=close_price)
                        results.append(price_data)

                    success = True
                except (requests.RequestException, ValueError) as e:
                    print(f"Error fetching data: {e}")
                    attempt += 1
                    if attempt < retries:
                        wait_time = 2 ** attempt
                        print(f"Retrying in {wait_time} seconds...")
                        time.sleep(wait_time)
                    else:
                        print(f"Failed to fetch data after {retries} attempts.")

            current_date += timedelta(days=1)

        return results
