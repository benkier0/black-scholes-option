# solved for volatility
# using root-finding

from scipy.optimize import brentq
from core.pricing import black_scholes_price
from typing import Literal

OptionType = Literal["call", "put"]

def implied_volatility(
    market_price: float,
    S: float,
    K: float,
    T: float,
    r: float,
    option_type: OptionType = "call",
    tol: float = 1e-5,
    max_iterations: int = 100
) -> float:
    """
    Solve for implied volatility using Brent's method.

    Returns:
        float: Implied volatility
    """

    def objective(sigma):
        return black_scholes_price(S, K, T, r, sigma, option_type) - market_price

    try:
        return brentq(objective, 1e-5, 5.0, xtol=tol, maxiter=max_iterations)
    except ValueError as e:
        raise RuntimeError(f"Failed to converge: {e}")
