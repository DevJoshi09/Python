# printing 
print("my name is dev");

# variables
# string
my_name = "dev";
print(my_name);

# f-string -> use to insert value between string
print(f"my name is {my_name}")

# boolean first letter of True/False will be capital
is_true = True

print(f"Are you a student ? : {is_true}")

# conditional statements
for_sale = True

if for_sale:
    print("The product is for sale")
else:
    print("product is not for sale")


# Type casting - converting a variable from one data type to another

name = "Dev"
age = 22
gpa = 7.75
is_student = True

age = str(age)
print(age)

# age+=1
gpa = int(gpa)
print(gpa)

# input() function used to take input from user as string 

name = input("Enter your name :")
age = input("Enter your age: ")

age = int(age)

print(f"Hi {name}")
print(f"your age is {age}")

# Excercise 1 - calculate the area of rectangle

length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter length of rectangle: "))

area = length * breadth
print(f"Area of Rectangle {length} * {breadth} = {area}")



# Excercise 2 - shoping cart program

item = input(f"Enter item you want to buy: ")
item_quantity = int(input(f"Enter item Quantity"))
price = float(input(f"Enter price of {item}"))

total = price * item_quantity;
print(f"you ordered {item_quantity} x {item} = ${total}")