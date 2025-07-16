# convert yahoo finance output into a clean structure

import pandas as pd
from typing import Literal

OptionType = Literal["call", "put"]

def clean_option_data(df: pd.DataFrame, option_type: str, expiry: str) -> list[dict]:
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
            "expiry": expiry,  # <-- assign correct expiry here
            "type": option_type
        })
    return cleaned
