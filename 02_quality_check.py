import pandas as pd
import numpy as np

# Read the data
df = pd.read_csv('./cleandata.csv')

# Count NaN values for each column
nan_count = df.isna().sum()

# Create a DataFrame with column names and corresponding NaN counts
nan_summary = pd.DataFrame({
    'Column Name': nan_count.index,
    'NaN Count': nan_count.values
})

# Print the DataFrame with column names and NaN counts
print("Summary of NaN values in each column:")
print(nan_summary)


# Map the data types for each column
dtypes_mapping = {
'ID'                                  : 'str',
'Age'                                 : 'object',
'Residence'                           : 'category',
'V-SE-Power'                          : 'int',
'V-SE-Achievement'                   : 'int',
'AVG-V-Self-Enhacemen'                : 'float',
'V-O-Hedonism'                         : 'int',
'V-O-Stimulation'                       : 'int',
'V-O-Self_direction'                    : 'int',
'AVG-V-Openness_to_change'            : 'float',
'V-ST-Universalism'                     : 'int',
'V-ST-Benevolence'                      : 'int',
'AVG-V-Self_transcendence'            : 'float',
'V-C-Tradition'                         : 'int',
'V-C-Conformity'                        : 'int',
'V-C-Security'                          : 'int',
'AVG-V-Conservation'                  : 'float',
'P-OX-Aesthetic_appreciation'            : 'int',
'P-OX-Inquisitiveness'                   : 'int',
'P-OX-Creativity'                        : 'int',                  
'P-OX-Unconventionality'                 : 'int',
'P-E-Liveliness'                        : 'int',
'AVG-P-Opennes_to_experience'           : 'int',
'P-E-Social_self-esteem'                : 'int',
'P-E-Social_boldness'                   : 'int',
'P-E-Sociability'                       : 'int',
'AVG-P-Extraversion'                  : 'float',
'P-HH-Modesty'                          : 'int',
'P-HH-Greed avoidance'                  : 'int',
'P-HH-Fairness'                         : 'int',
'P-HH-Sincerity'                        : 'int',
'AVG-P-Honesty-Humility'              : 'float',
'ATT-Favourable'                        : 'int',
'ATT-Smart'                             : 'int',
'AVG-ATT'                             : 'float',
'BEH-take_part'                         : 'int',
'BEH-passenger-usage'                 : 'int',
'PARTIC-YES-passenger-explanation'    : 'str',
'BEH-driver-usage'                    : 'int',
'PARTIC-YES-driver-explanation'        : 'str',
'INT-passenger'                       : 'int',
'INT-passenger-explanation'            : 'str',
'INT-driver'                         : 'int',
'INT-driver-explanation'               : 'str',
}

# Use astype to apply the data type changes
df = df.astype(dtypes_mapping)

print("\nData Types for Each Column:")
print(df.dtypes)






