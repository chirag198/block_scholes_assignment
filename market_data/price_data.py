from dataclasses import dataclass
from datetime import datetime


@dataclass
class PriceData:
    """
    Represents the closing price data for a specific date.

    Attributes:
        date (datetime): The date of the price data.
        closing_price (float): The closing price of the asset.
    """
    date: datetime
    closing_price: float

    @staticmethod
    def from_api_data(data: dict) -> "PriceData":
        """
        Converts API response data to PriceData.

        Args:
            data (dict): The data dictionary from the API response.

        Returns:
            PriceData: A PriceData instance with the parsed date and closing price.

        Raises:
            ValueError: If required data fields are missing in the response.
        """
        try:
            return PriceData(
                date=datetime.fromtimestamp(data['timestamp'] / 1000),
                closing_price=float(data['close'])
            )
        except KeyError as e:
            raise ValueError(f"Missing required field in data: {e}")
