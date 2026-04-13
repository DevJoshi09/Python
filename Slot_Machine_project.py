# Slot Machine
import random

def spin_row():
    symbols_list = ['🍒' , '🍉' , '🍋' , '🔔' , '⭐']
    
    # random_list = []
    # for symbols in range(3):
    #     random_list.append(random.choice(symbols_list))
    
    # # print(random_list)
    # return random_list;

    return [random.choice(symbols_list) for _ in range(3)]


def print_row(row):
    print(" ────────────── ")
    print("│ " + " │ ".join(row)+ " │")
    print(" ────────────── ")
    return 0

def get_payout(row , bet):

    if row[0] == row[1] == row[2] :
        if row[0] == '🍒':
            return bet*2
        elif row[0] == '🍉':
            return bet*3
        elif row[0] == '🍋':
            return bet* 4
        elif row[0] == '🔔':
            return bet*5
        else :
            return bet
        
    return 0

def main():

    print("************************************")
    print("***********Slot_Machine*************\n")
    # window + ;
    print("symbols : 🍒 , 🍉 , 🍋 , 🔔 , ⭐ \n")
    print("************************************")
    balance = 100

    while balance > 0 :
        bet = input("Enter amount in bet :")
        if not bet.isdigit():
            print("Enter a digit value")
            continue

        bet = float(bet)
        if bet <= 0 :
            print("Enter bet above 0")
            continue
        if bet > balance:
            print("Insufficiant Balance")
            continue
        else:
            balance -= bet
            ans = spin_row()
            print_row(ans)
            payout = get_payout(ans , bet)

            if payout > 0 :
                print(f"Your won {payout}")
            else:
                print("Sorry you lost this round")
                
            balance += payout

        if "n" == input("Do you want to continue (Y/N):") :
            break 
        
        print(f"Game Over ! Your current balance : {balance}")

if __name__ == "__main__":
    main()