# pulls option chains using api * likely yfinance
from pandas import DataFrame


def get_options_chain(ticker: str, expiry: str) -> dict:
    return {
        'calls': DataFrame,
        'puts': DataFrame
    }
