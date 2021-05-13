#!/usr/local/bin/python3

from forex_python.converter import CurrencyCodes, CurrencyRates

test = CurrencyRates()

#fetch the Conversion rate
rate = test.get_rate('SEK', 'INR')
print(rate)
