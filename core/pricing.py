# black-scholes closed form pricing + greeks

def black_scholes_price(S, K, T, r, sigma, option_type='call') -> float:
    ...

def greeks(S, K, T, r, sigma, option_type='call') -> dict:
    return {
        'delta': ...,
        'gamma': ...,
        'vega': ...,
        'theta':...,
        'rho': ...,
    }