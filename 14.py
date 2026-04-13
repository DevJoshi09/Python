# Exceptions :An event that intrupt the flow of program 
#       zeroDivisionError - when we try to divede a number by zero 
#       TypeError - when try to do operation between different data type ex : int and string
#       valueError- when we try to typecast  a value of wrong datatype ex: int("dev")

# Exception Handling: steps - try , except and finally

# try the code 
try:
    number = int(input("Enter a number: "))
    print(1/number)

# this will catch specific exception and tell the user
except ZeroDivisionError:
    print("your can't divide by zero idiot !")
except ValueError:
    print("you can't divide a number by another datatype")

# this will catch all exceptions 
except Exception:
    print("something went wrong !")

finally:
    print("Do some cleanup .")