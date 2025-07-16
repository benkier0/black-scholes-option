# convert yahoo finance output into a clean structure

import pandas as pd
from typing import Literal

OptionType = Literal["call", "put"]

def clean_option_data(
    df: pd.DataFrame,
    option_type: OptionType
) -> list[dict]:
    """
    Clean option chain data from Yahoo into a structured list of dicts.

    Example Output:
    [
        {
            'strike': 105.0,
            'lastPrice': 3.25,
            'impliedVol': 0.215,
            'expiry': '2025-07-18',
            'type': 'call'
        },
        ...
    ]
    """
    cleaned = []
    for _, row in df.iterrows():
        if row['impliedVolatility'] is None or pd.isna(row['impliedVolatility']):
            continue
        cleaned.append({
            "strike": row["strike"],
            "lastPrice": row["lastPrice"],
            "impliedVol": float(row["impliedVolatility"]),
            "bid": row.get("bid", None),
            "ask": row.get("ask", None),
            "expiry": row.get("lastTradeDate", None),
            "type": option_type
        })
    return cleaned
