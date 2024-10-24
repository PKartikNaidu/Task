# -*- coding: utf-8 -*-
"""kotak.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nnq42lANdSpSHgj0PH4Uj7BBzylCibFb
"""

import pandas as pd

# Load the files
kotak_cash = pd.read_csv('/content/KotakCash.csv', delimiter='|')
kotak_future_option = pd.read_csv('/content/Kotak_futureOption.csv', delimiter='|')

# Convert 'isin' to the same data type (string) in both datasets
kotak_cash['isin'] = kotak_cash['isin'].astype(str)
kotak_future_option['isin'] = kotak_future_option['isin'].astype(str)

# Merge the datasets on 'isin'
merged_kotak = pd.merge(kotak_cash, kotak_future_option, how='outer', on='isin')

# Save the merged file to a new CSV
merged_kotak.to_csv('Kotak_Merged.csv', index=False)

# Display the first few rows of the merged dataset
print(merged_kotak.head())

kotak_cash.info()

kotak_future_option.info()
