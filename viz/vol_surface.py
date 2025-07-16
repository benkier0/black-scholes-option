# plotly 3D surface using strike, expiry, and IV

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

def prepare_vol_surface_data(options: list[dict], valuation_date: datetime) -> pd.DataFrame:
    rows = []
    for opt in options:
        expiry_raw = opt.get("expiry", None)
        try:
            expiry = pd.to_datetime(expiry_raw).replace(tzinfo=None)
        except Exception as e:
            continue

        ttm_seconds = (expiry - valuation_date).total_seconds()
        ttm = ttm_seconds / (365.25 * 24 * 3600)
        if ttm <= 0:
            continue

        rows.append({
            "strike": opt["strike"],
            "ttm": ttm,
            "impliedVol": opt["impliedVol"],
        })

    df = pd.DataFrame(rows)
    print(f"Constructed DataFrame with shape: {df.shape}")
    return df



def plot_vol_surface(df: pd.DataFrame):
    """
    Plot implied volatility surface using Plotly.
    """
    # Create grid
    print("df_surface columns:", df.columns)
    print("df_surface head:\n", df.head())

    X = df['strike']
    Y = df['ttm']
    Z = df['impliedVol']

    fig = go.Figure(data=[go.Mesh3d(
        x=X,
        y=Y,
        z=Z,
        opacity=0.8,
        colorscale='Viridis',
        intensity=Z,
        showscale=True,
    )])

    fig.update_layout(
        scene=dict(
            xaxis_title='Strike Price',
            yaxis_title='Time to Maturity (Years)',
            zaxis_title='Implied Volatility'
        ),
        title='Implied Volatility Surface',
        margin=dict(l=0, r=0, b=0, t=40)
    )

    fig.show()
