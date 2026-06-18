## Grid Lines - reference line which add more clear readability to graph
import matplotlib.pyplot as plt

x= [1,2,3,4,5]
y= [5,10,15,20,25]

# plt.grid(axis="both",linewidth="1",color="grey",linestyle="dotted")
# plt.plot(x,y)
# plt.show()


## Bar Chart - Compare categories by representing each category as bars

fruits = ["apple","bannana","pineapple","guawa","orange"]
costs  = [100,60,120,120,150]


plt.yticks(costs)
plt.bar(fruits,costs,color="skyblue")

plt.title("Fruits Market Price",fontsize="23"
                        ,family="Arial"
                        ,fontweight="bold"
                        ,color="#2d4cfc")

plt.xlabel("Fruits",fontsize="20"
                   ,family="Arial"
                   ,fontweight="bold"
                   ,color="#2dbefc")

plt.ylabel("Price",fontsize="20"
                  ,family="Arial"
                  ,fontweight="bold"
                  ,color="#2dbefc")
plt.show()
