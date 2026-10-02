import pandas as pd

# DataFrame = A tabular data structure with rows AND columns. (2 Dimensional)
#             Similar to an Excel spreadsheet

data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "Age": [30, 35, 50]
}

# dataFrame = df meaning we are creating a DataFrame object

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"]) 

# print(df.loc["Employee 1"])
# print(df.iloc[1])

### Add a new column

df["Job"] = ["Cook", "N/A", "Cashier"]

### Add a new row

new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                        {"Name": "Eugene", "Age": 60, "Job": "Manager"}],
                        index=["Employee 4", "Employee 5"]) # Creating a new DataFrame for the new row


df = pd.concat([df, new_rows]) # adding the new row to the existing DataFrame

print(df)