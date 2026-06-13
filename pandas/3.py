# Filtering 
import pandas as pd

df = pd.read_csv("data.csv")
# print(df.columns)

# we want all tall pokemon data
tall_pokemon = df[df["Height"] >= 2]
# print(tall_pokemon)

# we want heavy pokemon
heavy_pokemon = df[df["Weight"] >= 100]
# print(heavy_pokemon)

# legendary pokemon
legend_pokemon = df[df["Legendary"] == 1]
# print(legend_pokemon)

# water pokemon
water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
# print(water_pokemon)

# fire and flying pokemon
ff_pokemon = df[(df["Type1"]=="Fire") & (df["Type2"]=="Flying")]
print(ff_pokemon)