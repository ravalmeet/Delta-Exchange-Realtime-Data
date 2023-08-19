Certainly! Here's the updated README format with the list of symbols separated by commas:

markdown
Copy code
# DeltaExAPI

## Introduction

DeltaExAPI is a Python module that provides a simple interface to interact with the Delta Exchange cryptocurrency derivatives exchange API. It allows you to access information about futures symbols, options symbols, and historical data for trading instruments.

## Installation

No installation is required for this module. You can simply import the `DeltaExAPI` class into your Python script.

```python
from DeltaExAPI import DeltaExAPI
```
Features

## List of Futures Symbols

The module includes a list of available futures symbols, which can be used for trading or data retrieval:

'BTCUSD', 'BCHUSDT', 'ETCUSDT', 'LINKUSDT', 'TRXUSDT', 'BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'LTCUSDT', 'BNBUSDT', 'ATOMUSDT', 'XTZUSDT', 'ETHBTC', 'VETUSDT', 'ALGOUSDT', 'SNXUSDT', 'DOTUSDT', 'UNIUSDT', 'COMPUSDT', 'AVAXUSDT', 'AAVEUSDT', 'XLMUSDT', 'ADAUSDT', 'XMRUSDT', 'SUSHIUSDT', 'DOGEUSDT', '1INCHUSDT', 'SOLUSDT', 'FILUSDT', 'MATICUSDT', 'CRVUSDT', 'SHIBUSDT', 'CHZUSDT', 'MANAUSDT', 'SANDUSDT', 'HBARUSDT', 'FTMUSDT', 'STXUSDT', 'NEARUSDT', 'DYDXUSDT', 'ARUSDT', 'RSRUSDT', 'ETHUSD', 'MKRUSDT', 'APEUSDT', 'OPUSDT', 'LDOUSDT', 'INJUSDT', 'APTUSDT', 'MASKUSDT', 'ARBUSDT', 'CFXUSDT', 'SUIUSDT', 'RNDRUSDT'

##List of Options Symbols

The module provides access to a list of available options symbols for trading:

'BTCUSDT', 'ETHUSDT'

##TimeFrames

The module supports various timeframes for historical data retrieval, including:

'1', '2', '3', '5', '15', '30', '45', '60', '120', '360', 'D' (daily)

##Usage

Retrieving Options Instruments

To retrieve options instruments for a specific symbol (e.g., 'BTC'), use the following code:

```python
options_data = DeltaExAPI.get_instruments_options('BTC')
```

##Retrieving Historical Data
To retrieve historical data for a specific symbol (e.g., 'BTCUSDT') with a given resolution (e.g., 'D' for daily) and a maximum time period (e.g., 7 days), use the 

following code:

```python
historical_data = DeltaExAPI.historical_data('BTCUSDT', 'D', 7)
```

## Retrieving Futures Instruments

To retrieve futures and perpetual futures instruments, use the following code:


```python
futures_data = DeltaExAPI.get_futures_instruments()
```
## Error Handling
The module includes basic error handling for network or API-related issues. It will print an error message in case of an error but won't raise an exception. You can customize the error handling within the class methods as needed.

## Disclaimer
Please consult Delta Exchange's official API documentation for usage policies, rate limits, and other guidelines. Use this module responsibly and in compliance with Delta Exchange's terms and conditions.

## License
This module is provided under the MIT License. See the LICENSE file for details.
