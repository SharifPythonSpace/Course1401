import pandas as pd

df = pd.read_csv('churn.csv')
print(df.info())
print(df.describe())
print(df.iloc[2].sum())
print('hello')