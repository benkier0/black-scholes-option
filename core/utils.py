# math helper fuctions, normal dist wrappers

import math

def d1(S, K, T, r, sigma):
    return (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))

def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * math.sqrt(T)

def normal_pdf(x):
    return math.exp(-x**2 / 2) / math.sqrt(2 * math.pi)
