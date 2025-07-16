import numpy as np
import matplotlib.pyplot as plt
from core.pricing import greeks

def plot_greek_vs_spot(K, T, r, sigma, greek='delta', option_type='call'):
    S = np.linspace(0.5*K, 1.5*K, 100)
    values = []

    for s in S:
        g = greeks(s, K, T, r, sigma, option_type)
        values.append(g[greek])

    plt.figure(figsize=(8, 5))
    plt.plot(S, values, label=f'{greek.capitalize()} ({option_type})')
    plt.xlabel('Spot Price')
    plt.ylabel(greek.capitalize())
    plt.title(f'{greek.capitalize()} vs Spot Price')
    plt.grid(True)
    plt.legend()
    plt.show()
