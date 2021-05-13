#!/usr/local/bin/python3

from forex_python.converter import CurrencyCodes, CurrencyRates
import pandas as pd

test = CurrencyRates()

#fetch the Conversion rate
rate = test.get_rate('SEK', 'INR')

data = {'Currency': [rate]} 

df = pd.DataFrame(data)

output = df.to_csv (mode = 'a', index = False, header=True)

df = pd.DataFrame(data, columns = ['Time', 'Currency'])
df.to_csv (r'data.csv', sep = '|', mode='a', index = False, header=True)
print (output)
