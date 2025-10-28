# collections : list , set , truple

# list
fruits= ["apple","orange","banana","mango","apple"]

# will only remove first occurance
# fruits.remove("apple")

for fruit in fruits:
    if fruit == "apple":
        fruits.remove(fruit)

print(fruits)

# set
# no duplicates allowed : will show only 1 occurance of every element
fruitss = {"apple","orange","banana","mango","apple"}
print(fruitss)

# shopping cart 

foods = []
prices = []
total = 0

while True :
    food = input("Enter your food (or q to quit) : ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food} : $"))
        prices.append(price)
        foods.append(food)

print("----your Cart-----")

# for food in foods :
#     print(f"{food},", end=" ")
print(foods)
for price in prices:
    total += price

print()
print(f"Your total price is : ${total}")

