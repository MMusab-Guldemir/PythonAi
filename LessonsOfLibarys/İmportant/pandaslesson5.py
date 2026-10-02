import pandas as pd

df = pd.read_csv(r"C:\Users\User\Desktop\PythonAi\LessonsOfLibarys\İmportant\data.csv", index_col="Name") # read_csv() is a function that reads a CSV file and creates a DataFrame object 

# SELECTION BY COLUMN

# print(df["Name"].to_string()) # print the "Name" column of the DataFrame
# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df[["Name", "Height", "Weight"]].to_string())

# SELECTION BY ROW/S

# print(df.loc["Charizard", ["Height", "Weight"]]) # print the row with index "Charizard" and the columns "Height" and "Weight"
# print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]]) # print the rows with index "Charizard" to "Blastoise" and the columns "Height" and "Weight"

# print(df.iloc[0:11]) # first 11 rows of the DataFrame 

# print(df.iloc[0:11:2]) # first 11 rows of the DataFrame with a step of 2
# print(df.iloc[0:11:2, 0:3]) # first 11 rows of the DataFrame with a step of 2 and the first 3 columns  -> yukarıdaki printle farklı olarak sadece ilk 3 kolonu alır 


pokemon = input("Enter a pokemon name: ") # get user input for a pokemon name

try:
    print(df.loc[pokemon]) # print the row with index equal to the user input
except KeyError: # if the user input is not a valid index, print an error message
    print(f" '{pokemon}' not found in the DataFrame.")