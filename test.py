from data.fetch_data import get_option_expiries, get_options_chain
from data.clean_data import clean_option_data
from viz.vol_surface import prepare_vol_surface_data, plot_vol_surface
from datetime import datetime

ticker = "AAPL"
valuation_date = datetime.today()

all_options = []

# Limit to first 3 expiry dates for speed
for expiry in get_option_expiries(ticker)[:3]:
    chain = get_options_chain(ticker, expiry)
    cleaned_calls = clean_option_data(chain["calls"], "call")
    all_options.extend(cleaned_calls)

df_surface = prepare_vol_surface_data(all_options, valuation_date)
plot_vol_surface(df_surface)
