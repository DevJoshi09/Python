import matplotlib.pyplot as plt
import numpy as np

# x = [2020,2021,2022,2023]
# y = [21,23,20,25]

x = np.array([2020,2021,2022,2023])
y1 = np.array([21,23,20,25])
y2 = np.array([12,18,24,10])
y3 = np.array([10,15,13,26])


# # 1->
plt.plot(x,y1,marker= "",markerfacecolor="red",markeredgecolor="red",
         linewidth=2,color="red")

plt.plot(x,y2,marker= "",markerfacecolor="blue",markeredgecolor="blue",
         linewidth=2,color="blue")

plt.plot(x,y3,marker= "",markerfacecolor="green",markeredgecolor="green",
         linewidth=2,color="green")

## 2->
# line_style = dict(marker=".",
#                   markersize= 10,
#                   markerfacecolor="red",
#                   markeredgecolor="red",
#                   linestyle="dotted",
#                   linewidth=2,
# )

# plt.plot(x,y1,color="blue", **line_style)
# plt.plot(x,y2,color="red" ,**line_style)


## ---- Labels ----

plt.title("Class Size",fontsize="25"
                      ,family="Arial"
                      ,fontweight="bold"
                      ,color="#2d4cfc")

plt.xlabel("Year",fontsize="20"
                    ,family="Arial"
                    ,fontweight="bold"
                    ,color="#2dbefc")

plt.ylabel("Student",fontsize="20"
                      ,family="Arial"
                      ,fontweight="bold"
                      ,color="#2dbefc")

# ticks - to display what we want to display in axis
plt.xticks(x)
plt.tick_params(axis="both",color="#2dbefc")
plt.show() 