# black-scholes-options

## Example Flow: Real-World Use Case
1. Get Market Data
    fetch_data.get_options_chain("AAPL", "2025-07-18")
    Clean it → list of strikes, market prices

2. Compute Implied Vol
    For each (S, K, T, r, market_price):
    implied_volatility(...)

3. Plot Vol Surface
    plot_vol_surface(...)

4. Price an Option
    black_scholes_price(S, K, T, r, sigma)
    View greeks(...)

5. Compare to Monte Carlo
    monte_carlo_price(...)
