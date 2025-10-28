# while loop

    # name = input("enter your name : ")

    # while name == "":
    #     print("you did not enter your name")
    #     name = input("enter your name : ");

    # print(f"Hi {name}")

    # age = int(input("Enter your Age : "))

    # while age<0 :
    #     print("Age can't be negative")
    #     age = int(input("Enter your Age : "))

    # print(f"your Age is : {age}")

# for loop

# digital clock count down

import time

my_time = int(input("Enter time in seconds : "))

for x in range(my_time,0,-1):
    seconds = int(x) % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time up !")