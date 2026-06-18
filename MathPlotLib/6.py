## SubPlot - It allows to display multiple graphs in the same figure.
import matplotlib.pyplot as plt
import numpy as np

# figure = the entire canva
# Ax = A single plot(Subplot)

x = np.array([0,1,2,3])

## Creating a sub plot of 2 row and 2 column
figure , axes = plt.subplots(2,2)

# 1 plot
axes[0,0].plot(x,x**2, color="blue")
axes[0,0].set_title("x**2")

# 2 bar
axes[0,1].bar(x,x**3, color="red")
axes[0,1].set_title("x**3")


# 3 pie chart
axes[1,0].pie(x, labels=x**4, autopct="%1.1f%%")
axes[1,0].set_title("x**4")


# 4 scatter
axes[1,1].scatter(x,x**5, color="yellow")
axes[1,1].set_title("x**5")

# this func will resolve overlaping issue between subplots
plt.tight_layout()

plt.show()
