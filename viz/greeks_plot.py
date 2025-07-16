import numpy as np
import matplotlib.pyplot as plt
from core.pricing import greeks
import streamlit as st 

def plot_greek_vs_spot(K, T, r, sigma, greek='delta', option_type='call'):
    S = np.linspace(0.5 * K, 1.5 * K, 100)
    values = []

    for s in S:
        g = greeks(s, K, T, r, sigma, option_type)
        values.append(g[greek])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(S, values, label=f'{greek.capitalize()} ({option_type})')
    ax.set_xlabel('Spot Price')
    ax.set_ylabel(greek.capitalize())
    ax.set_title(f'{greek.capitalize()} vs Spot Price')
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)  # streamlit rendering instead of plt.show()
