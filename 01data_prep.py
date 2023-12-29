import pandas as pd
import numpy as np

# Read the data
df = pd.read_csv('./data.csv')

# Replace NaN values with averages for specific columns
columns_to_replace = ['BEH-passenger-usage', 'BEH-driver-usage', 'INT-passenger', 'INT-driver']
for column in columns_to_replace:
    df[column].fillna(df[column].mean(), inplace=True)

    
# Save the cleaned DataFrame to cleandata.csv
df.to_csv('cleandata.csv', index=False)
print("\nDataFrame has been saved as cleandata.csv")