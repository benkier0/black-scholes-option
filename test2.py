from viz.greeks_plot import plot_greek_vs_spot

K = 100
T = 30 / 365
r = 0.01
sigma = 0.2

if __name__ == "__main__":
    for greek in ['delta', 'gamma', 'vega', 'theta', 'rho']:
        plot_greek_vs_spot(K, T, r, sigma, greek=greek, option_type='call')
