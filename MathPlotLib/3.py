import matplotlib.pyplot as plt

## Pie Chart = Used to show categry contibution to a whole (100%)

category = ["Freshers","Juniors","Seniors"]
values = [39,34,54]
colors = ["skyblue","green","orange"]

pie_style = dict(colors = colors,# to add color to slice of our choice
                 explode= [0,0.1,0],# to give slice outside effect
                 shadow= True, # to add shadow
                 startangle= 0)#for changing the angle of pie chart


#  note- autopct used for adding percentage to pie chart
plt.pie(values,labels= category,
        autopct="%1.2f%%", **pie_style)
plt.show()