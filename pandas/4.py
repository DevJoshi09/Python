# Aggregate function : reduce set of values to a single sumarry value

import pandas as pd 

df = pd.read_csv("data.csv") 

## for whole dataframe

mean_value = df.mean(numeric_only= True)
# print(mean_value)
sum_value = df.sum(numeric_only= True)
# print(sum_value)
min_value = df.min(numeric_only= True)
# print(min_value)
# print(df.count())

##  for single column

# print(f"{df["Height"].mean()} m")
# print(f"{df["Height"].sum()} m")
# print(f"{df["Height"].min()} m")
# print(f"{df["Height"].max()} m")

## using groupby() func

grp = df.groupby("Type1")
# print(grp["Weight"].mean())
# print(grp["Height"].mean())
# print(grp["Weight"].sum())
print(grp["Height"].count())
