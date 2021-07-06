
import pandas as pd
import numpy as np

original_dataset = pd.read_csv('data_100000.csv')
original_dataset.head(10)
print(original_dataset.head(10))

print(original_dataset.columns.tolist())

# drop all rows with any NaN and NaT values
original_dataset.dropna(inplace=True)


""" to remove the columns that are not relevant """
original_dataset.drop(columns=['off_street_name', 'cross_street_name', 'borough', 'location'], inplace=True)

"""To figure out if there are any missing value in the dataframe, 
and sum up the total for each column"""

print(original_dataset.columns.tolist())



