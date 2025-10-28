# dictionary : {key:value}

capitals = {"India":"New Delhi",
            "USA":"Washinton DC",
            "Japan":"Tokyo"}

# get value from key
# print(capitals.get("India"))

# update value
# capitals.update({"India":"Delhi"})

# delete key value
# capitals.pop("USA")

# delete last value
# capitals.popitem()


# print(capitals)

# to access both key and value
for key,value in capitals.items():
    print(f"{key :10} : {value}")

print("-----Menu-----")
# Task : Make Cafeteria menu counter

menu ={"pizza":"3.00",
       "nachose":"2.99",
       "popcorn":"5.00",
       "fries":"2.11"}

cart =[]
total = 0
for key,value in menu.items():
    print(f"{key :10}: ${value }")
print("--------------")

while True:
    food = input("Enter Food (or q to quit)").lower()

    if food == "q":
        break
    elif not menu.get(food) == None:
        cart.append(food)
        total += float(menu.get(food))
    else:
        print("Selected Food Item not in menu")


print()
print("------Your Order------")
for food in cart:
    print(food,end=", ")

print (f" = ${total}")