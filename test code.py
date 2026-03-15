import pandas as pd


df = pd.read_csv('psx_cache.csv')
data = df.values
heads = df.columns

print(heads)