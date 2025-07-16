import math
from scipy.stats import norm
from typing import Literal, Union

OptionType = Literal["call", "put"]

def d1(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Calculate the d1 component of Black-Scholes"""
    return (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))

def d2(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Calculate the d2 component of Black-Scholes"""
    return d1(S, K, T, r, sigma) - sigma * math.sqrt(T)

def black_scholes_price(
    S: float, K: float, T: float, r: float, sigma: float, option_type: OptionType = "call"
) -> float:
    """
    Calculate the Black-Scholes price for a European option.

    Parameters:
        S (float): Current stock price
        K (float): Strike price
        T (float): Time to expiration (in years)
        r (float): Risk-free interest rate (annual)
        sigma (float): Volatility of the underlying asset
        option_type (str): 'call' or 'put'

    Returns:
        float: Option price
    """
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d2(S, K, T, r, sigma)

    if option_type == "call":
        return S * norm.cdf(d_1) - K * math.exp(-r * T) * norm.cdf(d_2)
    elif option_type == "put":
        return K * math.exp(-r * T) * norm.cdf(-d_2) - S * norm.cdf(-d_1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

def greeks(
    S: float, K: float, T: float, r: float, sigma: float, option_type: OptionType = "call"
) -> dict[str, float]:
    """
    Calculate the Greeks for a European option.

    Returns:
        dict: delta, gamma, vega, theta, rho
    """
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d2(S, K, T, r, sigma)
    N_prime = lambda x: math.exp(-x**2 / 2) / math.sqrt(2 * math.pi)

    delta = (
        norm.cdf(d_1) if option_type == "call" else norm.cdf(d_1) - 1
    )

    gamma = N_prime(d_1) / (S * sigma * math.sqrt(T))
    vega = S * N_prime(d_1) * math.sqrt(T) / 100  # Per 1% change in vol
    if option_type == "call":
        theta = (-S * N_prime(d_1) * sigma / (2 * math.sqrt(T))
                 - r * K * math.exp(-r * T) * norm.cdf(d_2)) / 365
        rho = K * T * math.exp(-r * T) * norm.cdf(d_2) / 100
    else:
        theta = (-S * N_prime(d_1) * sigma / (2 * math.sqrt(T))
                 + r * K * math.exp(-r * T) * norm.cdf(-d_2)) / 365
        rho = -K * T * math.exp(-r * T) * norm.cdf(-d_2) / 100

    return {
        "delta": delta,
        "gamma": gamma,
        "vega": vega,
        "theta": theta,
        "rho": rho,
    }
