import pandas as pd
import numpy as np

# Read the data
df = pd.read_csv('./data.csv')

# Replace NaN values with averages for specific columns
columns_to_replace = ['BEH-passenger-usage', 'BEH-driver-usage', 'INT-passenger', 'INT-driver']
for column in columns_to_replace:
    df[column].fillna(df[column].mean(), inplace=True)



# Data Type Mapping
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
'P-E-Aesthetic_appreciation'            : 'int',
'P-E-Social_self-esteem'                : 'int',
'P-E-Inquisitiveness'                   : 'int',
'P-E-Social_boldness'                   : 'int',
'P-E-Creativity'                        : 'int',
'P-E-Sociability'                       : 'int',
'P-E-Unconventionality'                 : 'int',
'P-E-Liveliness'                        : 'int',
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


# Save the cleaned DataFrame to cleandata.csv
df.to_csv('cleandata.csv', index=False)
print("\nDataFrame has been saved as cleandata.csv")