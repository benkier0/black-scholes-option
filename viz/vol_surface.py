# plotly 3D surface using strike, expiry, and IV

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

def prepare_vol_surface_data(options: list[dict], valuation_date: datetime) -> pd.DataFrame:
    rows = []
    for opt in options:
        expiry = pd.to_datetime(opt["expiry"]).replace(tzinfo=None)  # <- make tz-naive
        ttm = (expiry - valuation_date).days / 365.0
        if ttm <= 0:
            continue
        rows.append({
            "strike": opt["strike"],
            "ttm": ttm,
            "impliedVol": opt["impliedVol"],
        })
    return pd.DataFrame(rows)


def plot_vol_surface(df: pd.DataFrame):
    """
    Plot implied volatility surface using Plotly.
    """
    # Create grid
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
