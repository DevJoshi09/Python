## Histogram - Used to show distribution of numerical data by grouping values into bins(intervals).
# It also count how many data falls in each range.

import matplotlib.pyplot as plt
import numpy as np

# This generate random 100 no
score = np.random.normal(loc=75,scale=15,size=100)
x = np.array([0,10,20,30,40,50,60,70,80])
# clip those score which are less than 0 and greater than 100
score = np.clip(score,0,100)

plt.hist(score,bins= 10,
              color="green",
              edgecolor="darkgreen")

plt.title("Exam Score")
plt.xlabel("Scores")
plt.ylabel("No of students")
plt.xticks(x)

plt.show()