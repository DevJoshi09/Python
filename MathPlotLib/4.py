# Scatter Graph- it shows relation between two numerical variables
# Helps to findcorrelation (+,-,None)

import matplotlib.pyplot as plt
import numpy as np

# marks of class 1
x1 = np.array([0,1,2,3,3,4,1])
y1 = np.array([54,53,56,67,76,85,51])

# marks of class 2
x2 = np.array([0,2,2,4,4,5])
y2 = np.array([53,61,63,68,71,88])

plt.scatter(x1,y1,color="skyblue",
                  alpha=1,# darkness / brightness of scatter color
                  s= 200,# size of scatter
                  label= "Class A")

plt.scatter(x2,y2,color="orange",
                  alpha=1,
                  s= 200,
                  label= "Class B")

plt.title("Test Score")
plt.xlabel("Hours Studied")
plt.ylabel("Grade")
# plt.grid()

## legend() function to show labels in graph
plt.legend()
plt.show()
