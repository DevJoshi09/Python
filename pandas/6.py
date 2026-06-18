# Pokemon Project - using pandas , matplotlib and numpy

import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

# creating a dataframe
df = pd.read_csv("data.csv")

# Creating a series of type_count of pokemon 
type_count = df["Type1"].value_counts(ascending=True)
# print(type_count)

plt.barh(type_count.index,type_count.values,color="skyblue",
                                            edgecolor="blue")

plt.title("Pokemon Type-Count", fontsize= 22,
                                family="Arial",
                                fontweight="bold",
                                color="black",
                               )
plt.xlabel("Count", fontsize= 12,
                                family="Arial",
                                fontweight="bold",
                                color="black",
                               )
plt.ylabel("Pokemon Type", fontsize= 12,
                                family="Arial",
                                fontweight="bold",
                                color="black",
                               )
plt.tight_layout()
plt.show()