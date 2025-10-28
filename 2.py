    # # string
    # username = input("Enter your name : ")

    # # check length of the username
    # if len(username) > 12 :
    #     print("username can't be greater than 12 characters")
    # # elif not username.find(" ") == -1 :
    # #     print("username can't contain spaces")
    # elif username.isalpha() == False:
    #     print("Username can only contain characters")
    # else :
    #     print(f"Welcome {username}")

#----------------------------------------------------------------- 
# string indexing
# question : print last 4 character of string

str = "1234-5678"

print(str[-4:])

credit_number = "1234-5678-9234"

print(f"xxxx-xxxx-{credit_number[-4:]}")