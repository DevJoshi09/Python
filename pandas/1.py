#PANDAS
import pandas as pd

#  SERIES - 1D Labeled array that can hold data of any datatype
data = [11,12,32,21]

# here series() is an constructor
ser = pd.Series(data,index = ["a","b","c"])
print(ser) 

# this will print data at particular index
print(ser.loc["a"])

print(ser[ser<15])

# example 
calories = {"Day 1":1750, "Day 2": 2100, "Day 3": 1700}
series = pd.Series(calories)
series.loc["Day 3"] += 500
print(series)
print(series[series<2000])

# ## DATAFRAME - 2D tabular data structure 

# its an dictionary 
Data = {
    "Name": ["dev","aditya","naman"],
    "Age" : [22,22,21]
}

#  converting to an df using constructor
df = pd.DataFrame(Data,index=[1,2,3])
# add new column
df["job"] = ["sde","N/A","cook"]
print(df)
# update index 2 job 
df.loc[2,'job'] = "junior_sde"
print(df)

print(" ")
# add new row
new_row = pd.DataFrame(
    [{"Name" : "Sandy", "Age": 23,"job": "duster"}],
    index= [4]
    )
df = pd.concat([df,new_row])
# add new rows
new_rows = pd.DataFrame(
    [{"Name": "jatin","Age": 19,"job":"developer"},
     {"Name": "suzuka","Age": 18,"job":"cs intern"},
     {"Name": "akash","Age": 20,"job":"data engineer"}],
     index=[5,6,7]
)
df = pd.concat([df,new_rows])
print(df)