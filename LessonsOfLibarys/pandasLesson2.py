import pandas as pd

calories = {"day1": 1750, "day2": 2180, "day3": 1700} # Creating a dictionary of data

series = pd.Series(calories, index=["day1", "day2", "day3"]) # Creating a series from the dictionary

# print(series) # Printing the series

series.loc["day3"] += 500 # Changing the value at index "day3" by adding 500 to it

# print(series.loc["day3"]) # Printing the value at index "day3"

print(series[series >= 2000]) # Accessing all values greater than or equal to 2000