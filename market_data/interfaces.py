from abc import ABC, abstractmethod


class MarketDataInterface(ABC):
    """
    Interface for fetching market data from an external source.
    """

    @abstractmethod
    def fetch_daily_closing_prices(self, start_date: str, end_date: str) -> list:
        """
        Abstract method to retrieve daily closing prices for a date range.

        Args:
            start_date (str): The start date in 'YYYY-MM-DD' format.
            end_date (str): The end date in 'YYYY-MM-DD' format.

        Returns:
            list: A list of price data for each day in the specified range.
        """
        pass
