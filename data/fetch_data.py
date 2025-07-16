# pulls option chains using api * likely yfinance
import yfinance as yf
import pandas as pd

def get_option_expiries(ticker: str) -> list[str]:
    """
    Get all available option expiry dates for a ticker.
    """
    t = yf.Ticker(ticker)
    return t.options  # list of expiry strings: ['2025-07-18', ...]

def get_options_chain(ticker: str, expiry: str) -> dict[str, pd.DataFrame]:
    """
    Fetch calls and puts for a given ticker and expiry.

    Returns:
        {'calls': DataFrame, 'puts': DataFrame}
    """
    t = yf.Ticker(ticker)
    chain = t.option_chain(expiry)
    return {
        "calls": chain.calls,
        "puts": chain.puts
    }

def get_underlying_price(ticker: str) -> float:
    """
    Get the latest price of the underlying asset.
    """
    t = yf.Ticker(ticker)
    return t.history(period="1d")["Close"].iloc[-1]
