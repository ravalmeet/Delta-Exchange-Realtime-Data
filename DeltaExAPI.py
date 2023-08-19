import pandas as pd
import json
import requests
from datetime import datetime, timedelta

class DeltaExAPI:
    def __init__(self):
        pass

    @staticmethod
    def get_today_and_tomorrow_dates_str():
        # Get today's date
        today = datetime.today().date()

        # Get tomorrow's date
        tomorrow = today + timedelta(days=1)

        next_tomorrow = today + timedelta(days=2)

        # Format dates as "ddmmyy"
        next_tomorrow_str = next_tomorrow.strftime('%d%m%y')
        tomorrow_str = tomorrow.strftime('%d%m%y')

        return tomorrow_str, next_tomorrow_str

    @staticmethod
    def get_instruments_options(symbol):
        url = f'https://cdn.deltaex.org/v2/tickers?contract_types=put_options,call_options,turbo_put_options,turbo_call_options'

        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(f"Error : {e}")

        r = response.json()

        r = r['result']

        df = pd.DataFrame(r)

        df = df[df['oi_value_symbol'] == symbol]

        df['date'] = df['symbol'].str.extract(r'-(\d+)$')

        tomorrow_str, next_tomorrow_str = DeltaExAPI.get_today_and_tomorrow_dates_str()

        filtered_df = df[(df['date'] == tomorrow_str) | (df['date'] == next_tomorrow_str)]

        filtered_df = filtered_df[['contract_type', 'mark_price', 'mark_vol', 'oi_contracts', 'oi_value_symbol', 'product_id', 'strike_price', 'symbol']]

        filtered_df = filtered_df.reset_index(drop=True)

        return filtered_df

    @staticmethod
    def historical_data(symbol, res, max_time):
        # Get the current timestamp
        curr_time = int(datetime.now().timestamp())

        today = datetime.now()

        # Calculate the start time based on the provided start_date
        start_time = today - timedelta(days=max_time)
        start_time = int(start_time.timestamp())

        url = f'https://cdn.deltaex.org/v2/chart/history?symbol=MARK%3A{symbol}&resolution={res}&from={start_time}&to={curr_time}&cache_ttl=10m'

        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(f"Error : {e}")

        r = response.json()

        r = r['result']

        df = pd.DataFrame(r)

        df['t'] = pd.to_datetime(df['t'], unit='s')

        return df

    @staticmethod
    def get_futures_instruments():
        url = f'https://cdn.deltaex.org/v2/tickers?contract_types=futures,perpetual_futures'

        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(f"Error : {e}")

        r = response.json()

        r = r['result']

        df = pd.DataFrame(r)

        return df

# Usage:
# delta_api = DeltaExAPI()
# options_data = delta_api.get_instruments_options('your_symbol_here')
# futures_data = delta_api.get_futures_instruments()
# historical_data = delta_api.historical_data('symbol', 'resolution', max_time)