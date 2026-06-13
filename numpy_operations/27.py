# RANDOME NUMBER GENERATOR
import numpy as np

rng = np.random.default_rng()
# print(rng.integers(low= 0,high= 90, size= (3,2)))


##  Floating point numbers - Decimal number
print(rng.uniform(low=0,high= 10,size=3))

# SHUFFLE ARRAY

arr = np.array([1,2,3,4,5])
rng.shuffle(arr)
print(arr)


# Randome choice
fruits = np.array(["apple","banana","mango","pineapple"])
fruit= rng.choice(fruits)
print(fruit)