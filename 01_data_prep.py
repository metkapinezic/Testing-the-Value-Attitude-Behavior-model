import pandas as pd
import numpy as np

df = pd.read_csv('./data/data.csv')

columns_to_replace = ['BEH-passenger-usage', 'BEH-driver-usage', 'INT-passenger', 'INT-driver']
for column in columns_to_replace:
    df[column].fillna(df[column].mean(), inplace=True)

    
df.to_csv('cleandata.csv', index=False)
print("\nDataFrame has been saved as cleandata.csv")