import pandas as pd

# df = pd.read_csv(r"C:\Users\User\Desktop\PythonAi\LessonsOfLibarys\İmportant\data.csv")
df = pd.read_json(r"C:\Users\User\Desktop\PythonAi\LessonsOfLibarys\İmportant\data.json") # read the data from a JSON file

print(df.to_string) # print the entire DataFrame without truncation
