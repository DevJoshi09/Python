# 2D list 

fruits =     ["apple","mango","banana"]
vegitables = ["lady finger","potatao","bringer"]
dairy =      ["milk","butter","Butter Milk"]

groceries = [fruits,vegitables,dairy]

for product in groceries:
    for food in product:
        print(food,end=" ")
    print()


# Task : Make mobile key pad

keyPad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

for row in keyPad:
    for key in row:
        print(key,end=" ")
    print()