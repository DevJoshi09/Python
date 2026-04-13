# python writing files(.txt ,.json ,.csv)
# -------------------------------------------

# ....txt files.... (only except string)

# # txt_data = "i like to code ! "
# employees = ["xx","xy","yx","yy"]

# file_path = "2.test.txt"

# with open(file= file_path,mode="a")as file:
#     # file.write("\n" + txt_data)
#     file.write("\n")
#     for emp in employees:
#         file.write(emp +" ")

#     print(f"file {file_path} is created ")

# ---------------------------------------------------------

# ....json.... (Made of key value pairs)

# import json
# # dictionary of employes
# employee = {
#     "name":"xy",
#     "age":28,
#     "job":"cook"
# }

# file_path= "2output.json"

# try:
#     with open (file_path,"w")as file:
#         # this will convert dictionary to json string. 
#         # 1 attribute- dictionary you want to save , 2 - where you want to save , 3 - indentation
#         json.dump(employee,file,indent=4)
#         print(f"{file_path} is created")
# except FileExistsError:
#     print("That file already exists.")


# -----------------------------------------------------------------------

# csv file are used to save 2d data 
import csv

file_path = "2_3_output.csv"
public_data = [["Name","Age","Job"],
               ["Aditya",22,"unemployed"],
               ["Dev",23,"unemployed"],
               ["Gaurav",23,"Tcs"],
               ["Naman",21,"Infosys"]
               ]

try :
    with open(file_path,"w",newline="") as file:
        # created a csv file
        writer = csv.writer(file)
        # to input values in csv file
        for row in public_data:
            writer.writerow(row)

        print(f"CSV file {file_path} was created.")
except FileExistsError:
    print("file already exists.")
