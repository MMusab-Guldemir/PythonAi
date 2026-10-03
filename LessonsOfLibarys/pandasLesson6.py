import pandas as pd

df = pd.read_csv(r"C:\Users\User\Desktop\PythonAi\LessonsOfLibarys\data.csv") # read_csv() 

# Filtering d= Keeping the rows that match a condition

tall_pokemon = df[df["Height"] >= 2]

heavy_pokemon = df[df["Weight"] >= 100]

# legendary_pokemon = df[df["Legendary"] == 1]
# legendary_pokemonT = df[df["Legendary"] == True]             # The Data 0 and 1 are used to represent False and True

# water_pokemon = df[(df["Type1"] == "Water") |
#                    (df["Type2"] == "Water")] # keep the rows where the "Type 1" or "Type 2" column is equal to "Water"

# tall_and_heavy_pokemon = df[(df["Height"] >= 2) & (df["Weight"] >= 100)] # & is the logical AND operator

# print(tall_pokemon.to_string()) # print the DataFrame with the rows that match the condition

ff_pokemon = df[(df["Type1"] == "Fire") &
                (df["Type2"] == "Flying")]

print(ff_pokemon.to_string()) # print the DataFrame with the rows that match the condition

