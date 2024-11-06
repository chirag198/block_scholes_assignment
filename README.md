# Block Scholes Assignment: Market Data Fetcher

This project provides a Python solution to fetch historical BTC-USD daily closing prices for the month of July 2024 from OKX's public REST API. The fetched data includes timestamps in UTC format and daily closing prices, organized as a reusable component for potential use in a production environment.

## Features

- **Data Retrieval**: Fetches BTC-USD daily closing prices from OKX’s API.
- **Error Handling**: Retries with exponential backoff for failed requests.
- **Modular Design**: Encapsulates functionality in classes for flexibility and reusability.
- **Testing**: Unit tests and integration tests validate functionality and API interaction.

## Requirements

- Python 3.7 or higher
- Access to the OKX public API for retrieving BTC-USD historical data.

## Setup

1. **Clone the repository**:
   ```bash
   git clone git@github.com:chirag198/block_scholes_assignment.git
   cd block_scholes_assignment

2. Activate env
    ```bash
   python3 -m venv venv
   source venv/bin/activate
   
3. Install dependencies:
    ```bash
   pip install -r requirements.txt

## Usage
To run the main program to fetch data for July 2024:
   ```bash
   python main.py
```
## Sample Output
```2024-07-01: $30300.0
2024-07-02: $31000.0
...
2024-07-31: $29000.0
```

## Running Tests

- **Unit and integration tests are available to validate the core functionalities of the MarketDataFetcher. Tests use the unittest framework, with mock API responses.**

### Run all tests:
   ```bash
   python -m unittest discover -s tests
   ```
### Run individual test file:
   ```bash
   python -m unittest tests/test_market_data_fetcher.py
   ```

## Code Structure

- **MarketDataFetcher**: Main class responsible for fetching data from the OKX API.
- **PriceData**: Model class encapsulating date and closing price.
- **Tests**: Both unit tests with mocked API responses and integration tests with actual data retrieval.

## API Documentation

This project interfaces with OKX's public REST API for fetching historical data. No API keys are required.

- **Base URL**: `https://okx.com/api/v5/market/history-candles`
- **Parameters**:
  - `instId`: Set to `"BTC-USD-SWAP"` for BTC-USD historical prices.
  - `bar`: Set to `"1D"` for daily intervals.
  - `before`: Timestamp in milliseconds, indicating the latest time for which data is retrieved.

## Conclusion

This project provides a foundational system for fetching historical BTC-USD daily closing prices from OKX’s public API, supporting data parsing, validation, and error handling for a production-like setup. With modular classes and testing included, this setup ensures data reliability and extensibility for further development.

Thank you for reviewing this project! Please feel free to reach out with any questions or feedback.

Happy coding!
