import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from core.pricing import black_scholes_price, greeks
from viz.greeks_plot import plot_greek_vs_spot  # reused for subplot
import seaborn as sns

st.set_page_config(page_title="Black-Scholes Option Pricing", layout="wide")

st.title("💹 Black-Scholes Option Dashboard")

# --- Sidebar Ticker Input ---
st.sidebar.header("🔍 Ticker & Option Settings")

ticker = st.sidebar.text_input("Ticker", "AAPL").upper()
option_type = st.sidebar.selectbox("Option Type", ["call", "put"])

# --- Fetch Stock Info ---
try:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="6mo")
    spot_price = hist["Close"].iloc[-1]
except Exception as e:
    st.error(f"Error fetching data for {ticker}")
    st.stop()

st.sidebar.markdown(f"**Spot Price**: ${spot_price:.2f}")

# --- Expiry Picker ---
options_dates = stock.options
expiry_str = st.sidebar.selectbox("Expiry", options_dates)
expiry = datetime.strptime(expiry_str, "%Y-%m-%d")
T = (expiry - datetime.today()).days / 365

# --- Manual Sliders ---
K = st.sidebar.slider("Strike Price (K)", 0.5 * spot_price, 1.5 * spot_price, spot_price)
r = st.sidebar.slider("Risk-Free Rate (%)", 0.0, 10.0, 1.0) / 100
sigma = st.sidebar.slider("Volatility (%)", 1.0, 100.0, 20.0) / 100

# --- Price Calculation ---
st.subheader("📊 Black-Scholes Output")

price = black_scholes_price(spot_price, K, T, r, sigma, option_type)
st.metric(label="Option Price", value=f"${price:.2f}")

greek_vals = greeks(spot_price, K, T, r, sigma, option_type)
greek_cols = st.columns(5)
for col, g in zip(greek_cols, greek_vals):
    col.metric(g.capitalize(), f"{greek_vals[g]:.4f}")

# --- Greeks Grid Plot ---
st.subheader("📉 Greeks vs Spot Price")

S_range = np.linspace(0.5 * spot_price, 1.5 * spot_price, 100)

fig, axes = plt.subplots(2, 3, figsize=(16, 8))
greek_names = ['delta', 'gamma', 'vega', 'theta', 'rho']

for ax, greek in zip(axes.flatten(), greek_names):
    values = []
    for s in S_range:
        g = greeks(s, K, T, r, sigma, option_type)
        values.append(g[greek])
    ax.plot(S_range, values, label=greek.capitalize())
    ax.set_title(f"{greek.capitalize()} vs Spot")
    ax.grid(True)

fig.delaxes(axes[1, 2])  # remove extra subplot
st.pyplot(fig)

# --- Historical Volatility Chart ---
st.subheader("📈 Historical Volatility (30-day Rolling)")

hist['log_return'] = np.log(hist['Close'] / hist['Close'].shift(1))
hist['volatility'] = hist['log_return'].rolling(window=30).std() * np.sqrt(252)

vol_fig, vol_ax = plt.subplots(figsize=(12, 4))
vol_ax.plot(hist.index, hist['volatility'], color='purple')
vol_ax.set_title("Rolling 30-Day Historical Volatility")
vol_ax.set_ylabel("Volatility")
vol_ax.grid(True)

st.pyplot(vol_fig)
