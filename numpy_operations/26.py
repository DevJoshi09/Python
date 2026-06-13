# filtering - selecting elements that matches some specific conditions
  
import numpy as np

ages = np.array([[11,12,23,41,15,18,19],
                 [61,77,78,98,65,66,34]])

##  Normal filtering
# teenagers = ages[ages < 18]
# adults = ages[(ages >= 18) & (ages < 65) ]
# seniors = ages[ages >=65]
# even_age = ages[ages % 2 == 0]
# odd_age = ages[ages % 2 != 0]

# tenager_senior = ages[(ages < 18) | (ages >= 65)]

# print(tenager_senior)

# ## WHERE Filtering
adult = np.where((ages>= 18) & (ages < 65), ages, 0)
print(adult)
