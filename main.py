from collections import Counter

from market_data.market_data_fetcher import MarketDataFetcher


def main():

    fetcher = MarketDataFetcher()
    prices = fetcher.fetch_daily_closing_prices("2024-07-01", "2024-07-31")

    for price in prices:
        print(f"{price.date}: {price.closing_price}")


if __name__ == "__main__":
    main()
