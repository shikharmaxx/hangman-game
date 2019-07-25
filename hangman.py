
from random import choice
import asciihangman

print("------------------------LETS PLAY HANGMAN ------------------------ ")
print("choose level of difficulty ->")
print(" [easy]\n [medium] \n [hard] ")
while True: 
    
    val = input("please enter your choice :").upper()

    if val == "EASY".upper():
        file = open('C:/Users/shikh/Desktop/Python VScode/hangman project/easy.txt' , 'r')
        break
    elif val == "MEDIUM".upper():
        file = open('C:/Users/shikh/Desktop/Python VScode/hangman project/medium.txt' , 'r')
        break
    elif val == "HARD".upper():
        file = open('C:/Users/shikh/Desktop/Python VScode/hangman project/hard.txt' , 'r')
        break
    else:
        print("invalid choice enter again !! ")

wordlist = file.read().upper().splitlines()
secret_word = choice(wordlist)
correct =[]
incorrect = []

#print("DEBUG :" , secret_word)

def draw_board():
    print('____________________________________________________________')
    print(asciihangman.hangman_board[len(incorrect)])
    print("\n")
    for i in secret_word:
        if i in correct:
            print(i,end=" ")
        else :
            print('_',end=" ")
    print("\n")


def user_guess():
    while True:
        guess = input("Guess a letter : ").upper()
        if guess in correct or guess in incorrect:
            print("You have already guessed that letter. Guess Again !!")
        elif guess.isnumeric():
            print("Please enter only letters. Guess Again !!")
        elif len(guess) > 1:
            print("Please guess only one letter at a time. Guess Again !! ")
        elif len(guess) == 0:
            print("Please enter ur selection.")
        else :
            break
    if guess in secret_word:
        correct.append(guess)
    else:
        incorrect.append(guess)
        
def check_win():
    if len(incorrect)>5:
        return "loss"
    for i in secret_word:
        if i not in correct:
            return 'not win'
    return 'win'

while True:
    draw_board()
    user_guess()
    
    win_condition = check_win()
    if win_condition == 'loss':
        print("\n******************************************")
        print(asciihangman.hangman_board[6])
        print("\nGAME OVER :(")
        print("The correct word was '" , secret_word ,"' ")
        print("******************************************")
        break
    elif win_condition == 'win':
        print("\n******************************************")
        print("VICTORY :) ")
        print("The word was '" , secret_word ,"' ")
        print("******************************************")
        break
input()
