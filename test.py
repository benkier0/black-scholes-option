from data.fetch_data import get_options_chain, get_underlying_price
from data.clean_data import clean_option_data

ticker = "AAPL"
expiry = "2025-07-18"

# Fetch raw data
chains = get_options_chain(ticker, expiry)
spot = get_underlying_price(ticker)

# Clean both call and put chains
calls = clean_option_data(chains["calls"], "call")
puts = clean_option_data(chains["puts"], "put")

print("Spot price:", spot)
print("First call option:", calls[0])
