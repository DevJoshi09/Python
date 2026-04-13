# Date AND Time

import datetime

#to insert a date 
d = datetime.date(2026,1,2)
print(d)
# current date
today = datetime.date.today()
print(today)

# to insert time-hr,min,sec
t = datetime.time(12,30,5)
print(t)
# current time
now = datetime.datetime.now()

# printing in string format
now = now.strftime("%H:%M:%S %d-%m-%Y")
print(now)

