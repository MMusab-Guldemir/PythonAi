import pandas as pd

# Series = A Pandas 1-Dimensional labeled array that can hold any data type
#           Think of it like a single column in a spreadsheet (1-Dimensional)

data = [100, 102, 104, 200, 202] # Creating a list of data

series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e']) # Changing index to a, b, c, d, e instead of 0, 1, 2, 3, 4

# series.loc["c"] = 200 # Changing the value at index 'c' to 200

# print(series.iloc[1]) # Accessing the value at index 1 (which is 'b')

# print(series.loc['a']) # Accessing the value at index 'a'

print(series[series >= 200]) # Accessing all values greater than 200 or equal to 200

