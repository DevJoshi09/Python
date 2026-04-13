# python reading files (.csv, .json, .csv)

# .txt file
# file_path = "1.test.txt"

# try:
#     with open (file_path,"r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found....")    
# except PermissionError:
#     print("permession denied...")

# ------------------------------------------

# .json
# import json

# file_path = "2output.json"

# try:
#     with open (file_path,"r") as file:
#         content = json.load(file)
#         print(content)
#         # print(content["name"])
# except FileNotFoundError:
#     print("File not found....")    
# except PermissionError:
#     print("permession denied...")

# --------------------------------------------

# .csv

import csv 

file_path = "2_3_output.csv"



try:
    with open (file_path,"r") as file:
        content = csv.reader(file)
        # this will return the memory address
        # print(content)
        # because all the data in csv file is in form of collection we have to iterate every line
        for row in content:
            print(row)
            # print(row[0])
except FileNotFoundError:
    print("File not found....")    
except PermissionError:
    print("permession denied...")