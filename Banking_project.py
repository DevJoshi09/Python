# Banking Program 

def show_balance(balance):
    print(f"Balance : {balance: .2f} Rs")


def deposite():

    amount = float(input("Enter amount to be deposite :"))
    if amount < 0 :
        print("******************")
        print("Enter Valid amount...")
        print("******************")
        return 0
    else :
        return amount


def withdraw(balance):
    amount = float(input("Enter amount to Witdraw :"))
    if amount < 0 or amount > balance :
        print("******************")
        print("Invalid amount...")
        print("******************")
        return 0
    else:
        return amount 
    

def main():

    balance = 0
    is_running = True


    while is_running :
        print("******************")
        print("******************")
        print("Bank Program ")
        print("******************")

        print("******************")
        print("1. Check Balance ")
        print("2. Deposite ")
        print("3. Withdraw ")
        print("4. Exit")
        print("******************")

        Choice = input("Enter your choice (1-4):")

        if Choice == '1':
            show_balance(balance)
        elif Choice == '2':
            balance += deposite()
        elif Choice == '3':
            balance -= withdraw(balance)
        elif Choice == '4':
            is_running = False
        else :
            print("Enter valid option...")

    print("******************")
    print("     Thank You      ")
    print("******************")



if __name__ == "__main__":
    main()