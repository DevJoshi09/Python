# Multithreading- Used to perform multiple task concurrently 

import threading
import time

def take_dog_for_walk(first,last):
    time.sleep(4)
    print(f"you finished walking {first} {last}")

def take_trash_out(trash_no):
    time.sleep(2)
    print(f"taken trash no {trash_no} out to garbage")

def take_mail_out():
    time.sleep(1)
    print("recieving mail from mail box")

dog_first_name = input("enter dogs first name : ")
dog_last_name = input("enter dogs second name : ")

trash_number = input("enter trash number : ")

t1 = threading.Thread(target= take_dog_for_walk, args=(dog_first_name,dog_last_name))
t1.start()
t2 = threading.Thread(target= take_trash_out, args=(trash_number,))
t2.start()
t3 = threading.Thread(target= take_mail_out)
t3.start()

# using .join methord so main methord will wait for them to complete
t1.join()
t2.join()
t3.join()

time.sleep(1)
print("All work are completed !!")