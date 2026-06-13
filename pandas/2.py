# read files like txt, json and csv 
import pandas as pd

df = pd.read_csv("data.csv")

# df = pd.read_json("data.json")

print(df.to_string())

## SELECTION BY COLUMN
print(df["Name"].to_string())
print(df["Height"].to_string())

# SELECTING MULTIPLE COLUMNS
print(df[["Name","Height","Weight"]].to_string())


## SELECTION BY ROWS

print(df.loc[0])

# IF WE KNOW A POKEMON BY ITS NAME 
df = pd.read_csv("data.csv",index_col="Name")

print(df.loc["Pikachu"])
print(df.loc["Charizard",["Height","Weight"]])

# SELECT ALL POKEMON BETWEEN PIKACHU AND CHARIZARD
print(df.loc["Charizard":"Pikachu", ["Height","Weight"]].to_string())
# print(df.loc[0:10,["Name","Height","Weight"]].to_string())

# we can also access through index , iloc[start:end:steps, start:end]
#                                        [no. of columns , no. of rows]
print(df.iloc[0:11].to_string())



# # Take input from user 
pokemon = input("Enter a pokemon name (*first letter capital) : ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(F"{pokemon} not found")