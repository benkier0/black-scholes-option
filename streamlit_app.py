import streamlit as st
import numpy as np
from datetime import date, timedelta

from core.pricing import black_scholes_price, greeks
from viz.greeks_plot import plot_greek_vs_spot

st.set_page_config(page_title="Black-Scholes Option Pricing", layout="centered")

st.title("📈 Black-Scholes Option Pricing Dashboard")

# --- Sidebar Inputs ---
st.sidebar.header("Option Parameters")

option_type = st.sidebar.selectbox("Option Type", ["call", "put"])
S = st.sidebar.slider("Spot Price (S)", 50.0, 200.0, 100.0)
K = st.sidebar.slider("Strike Price (K)", 50.0, 200.0, 100.0)
T_days = st.sidebar.slider("Time to Expiry (days)", 1, 365, 30)
T = T_days / 365
r = st.sidebar.slider("Risk-Free Rate (%)", 0.0, 10.0, 1.0) / 100
sigma = st.sidebar.slider("Volatility (%)", 1.0, 100.0, 20.0) / 100

# --- Pricing Output ---
st.subheader("📊 Option Price")
price = black_scholes_price(S, K, T, r, sigma, option_type)
st.metric(label="Black-Scholes Price", value=f"${price:.2f}")

# --- Greeks Output ---
st.subheader("⚙️ Greeks at Current Parameters")
greek_vals = greeks(S, K, T, r, sigma, option_type)

cols = st.columns(5)
for col, name in zip(cols, ['delta', 'gamma', 'vega', 'theta', 'rho']):
    col.metric(label=name.capitalize(), value=f"{greek_vals[name]:.4f}")

# --- Plotting Greeks ---
st.subheader("📉 Greeks vs Spot Price")

greek_to_plot = st.selectbox("Select Greek to Plot", ['delta', 'gamma', 'vega', 'theta', 'rho'])

plot_greek_vs_spot(K, T, r, sigma, greek=greek_to_plot, option_type=option_type)
