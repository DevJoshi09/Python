# Data Cleaning : the process of fixing or removing : incomplete , incorrect or irrelevant data . 
# ~75% work done with pandas i data cleaning

import pandas as pd

df = pd.read_csv("data.csv")

## 1. drop irrelevant column
# df = df.drop(columns=["No","Legendary"])


## 2. handle missing data- by droping or by filling
# df = df.dropna(subset=["Type2"])
# df= df.fillna({"Type2":"None"})



## 3. Fix inconsistant values

# df["Type1"] = df["Type1"].replace({"Grass":"GRASS",
#                                    "Water":"WATER",
#                                     "Fire":"FIRE",
#                                     "Rock":"ROCK"})


## 4. Standardize text
# df["Name"] = df["Name"].str.upper()    



## 5. Fix data type
# df["Legendary"] = df["Legendary"].astype(bool)



## 6. Remove duplicate values
df = df.drop_duplicates()

print(df.to_string())