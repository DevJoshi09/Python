# Hangman - A game in which we have to guess the hidden word letter and if we give 6 incorrect guess we loose.

import random



# Tuple(ordered, unchangable) of words which we have to guess.
words = ("apple","orange","banana","pineapple")


HangMan_art = {0 :  ("   ",
                     "   ",
                     "   "),
                1 : (" o ",
                     "   ",
                     "   "),
                2 : (" o ",
                     " | ",
                     "   "),
                3 : (" o ",
                     "/| ",
                     "   "),
                4 : (" o ",
                     "/|\\",
                     "   "),
                5 : (" o ",
                     "/|\\",
                     "/  "),
                6 : (" o ",
                     "/|\\",
                     "/ \\")
                    }
    

def guess(letter,word,visited,n):
    for i in range(n):
        if letter == word[i] and visited[i] == 0 :
            visited[i] = 1
            return i
        
    return -1

def display_man(x):
    # HangMan Art 
    for line in HangMan_art[x]:
        print(line)


def main():

    # for i in range(n):
    #     temp +="_"

    word = random.choice(words)
    print(word)
    n = len(word)
    temp = "_" * n
    # changing string to a list because string are imutable in python
    word_lst = list(temp)
    visited = [0]*n
    incorrect_guess = 0
    correct_guess = 0

    print(" ".join(word_lst))

    while incorrect_guess < 6 and correct_guess < n :
        
        display_man(incorrect_guess)
        letter = input("Guess the Letter: ")
        index = guess(letter,word,visited,n)

        if index != -1 :
            word_lst[index] = letter
            correct_guess += 1
            print(" ".join(word_lst))

        else :
            incorrect_guess += 1
            print("wrong guess...")
            

    if incorrect_guess >= 6:
        print("you Lost !!")
        display_man(6)
    else:
        print("You Guessed the correct word....!")


if __name__ == "__main__" :
    main()