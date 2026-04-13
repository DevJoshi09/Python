# functions

def Print(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

first = input("Enter your first name : ")
last = input("Enter your last name : ")
name = Print(first,last)

print(name)

# default function - default value is pass if no value passed

def net_price(amount, discount=0, tax=0.05):

    return amount + (1-discount) + (1+tax)

print(net_price(100))
    

import time

def count(start=0,end=10):
    for x in range(start,end+1):
        print(x)
        time.sleep(0.05)
print("Done!")

count(1,10)


# keyword argument : defines argument title outside and the argument placement dosen't matters

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello(greeting="Hi", title="the", first="dev", last="joshi")


#  Arbitary function
# *args= used to take multiple non key argument as parameter in function -> args is a tuple
# you can also change the args name ex: *nums , names etc;
# 
# 
# syntax : *args

def add(*args):
    sum = 0
    for x in args:
        print(x, end=" ")

add("1","2","3")


# ** kwargs -> allows to pass multiple keywords arguments
# kwargs is an dictionary

function
def add_address(**kwargs):
    # print(type(kwargs))
    # for key in kwargs.keys():
    #     print(key,end=" ")
    # print()
    # for val in kwargs.values():
    #     print(val,end=" ")

    for key, value in kwargs.items():
        print(f"{key} : {value}")


# function call
add_address(street="xyz",city="yyy",state="xxz",country="zzz")


# Task: using both *args and **kwargs together

def shipping_label(*args,**kwargs):

    for arg in args:
        print(arg,end=" ")

    print()
    print("------- address ---------")
    for key , value in kwargs.items():
        print(f"{key} : {value}")



shipping_label("Mr.","dev","joshi",street="xyz",city="yyy",state="xxz",country="zzz")