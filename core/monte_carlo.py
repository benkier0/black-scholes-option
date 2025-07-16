# monte carlo pricing for euro + exotic options

import numpy as np
from typing import Literal

OptionType = Literal["call", "put"]

def monte_carlo_price(
    S: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    n_simulations: int = 100_000,
    option_type: OptionType = "call",
    seed: int = 42
) -> float:
    """
    Monte Carlo simulation to estimate European option price.

    Returns:
        float: Estimated option price
    """
    np.random.seed(seed)
    Z = np.random.standard_normal(n_simulations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    if option_type == "call":
        payoff = np.maximum(ST - K, 0)
    elif option_type == "put":
        payoff = np.maximum(K - ST, 0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return np.exp(-r * T) * np.mean(payoff)

