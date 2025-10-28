# randome numbers library

import random

# # lowest and highest number 
# low = int(input("Enter starting number : "))
# high = int(input("Enter End number : "))

# random_number = random.randint(low,high)

# count = 0

# while True:

#     ans = int(input("Enter your guess number : "))
#     count+=1
#     if ans < random_number or ans > random_number :
#         print(f"Select numbers beteen {low} - {high}")

#     elif random_number == ans :
#         print(f"You guess the Correct Number in {count} guesses...!")
#         break

#     else:
#         print("Hard Luck Try again...")
#         help = input("Do you need help (y/n)?").lower()
#         if help == "y":
#             if ans < random_number:
#                 print("your answer is smaller than randome answer")
#             else:
#                 print("your answer is greater than randome answer")




# Game : Rock , paper and scissor

options = ("rock","paper","scissor")



rounds = int(input("Enter rounds off : "))



My_point = 0
computer_point = 0

for round in range(rounds):
    if My_point > rounds/2 or computer_point > rounds/2 :
        break

    player = input("Enter your choice (rock or paper or scissor) : ").lower()
    computer = random.choice(options)

    if player == "rock" and computer == "scissor":
        print(f"{player} / {computer}")
        My_point += 1

    elif player == "paper" and computer == "rock":
        print(f"{player} / {computer}")
        My_point += 1

    elif player == "scissor" and computer == "paper":
        print(f"{player} / {computer}")
        My_point += 1

    elif player == computer:
        print(f"{player} / {computer}")
        round -= 1
        
    else:
        print(f"{player} / {computer}")
        computer_point += 1

if My_point > computer_point:
    print(f"You won the match by {My_point}-{computer_point}")
elif My_point == computer_point:
    print("Match Draw...")
else:
    print("You Lost the Match ...")