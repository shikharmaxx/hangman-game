
from random import choice 
wordlist = 'airplane car television speaker computer'.upper().split()


hangman_board =[
    '''   
    /-----\\
          |
          |
          |
          |
     _____|''',
    '''      
    /-----\\
    O     |
          |
          |
          |
     _____|''',
    '''
    /-----\\
    O     |
    |     |
          |
          |
     _____|''',
    '''
    /-----\\
    O     |
   \|     |
          |
          |
     _____|''',
    '''
    /-----\\
    O     |
   \|/    |
          |
          |
     _____|''',
    '''
    /-----\\
    O     |
   \|/    |
    |     |
   /      |
     _____|''',
    ''' 
    /-----\\
    O     |
   \|/    |
    |     |
   / \    |
     _____|'''
               ]


secret_word = choice(wordlist)
correct =[]
incorrect = []

print("DEBUG :" , secret_word)

def draw_board():
    print('____________________________________________________________')
    print(hangman_board[len(incorrect)])
    print("\n")
    for i in secret_word:
        if i in correct:
            print(i,end=" ")
        else :
            print('_',end=" ")
    print("\n")
    

    #print("--------------MISSED LETTERS-------------------")
    #for i in incorrect:
     #   print( i ,end=" ")
    #print("\n-----------------------------------------------")

def user_guess():
    while True:
        guess = input("Guess a letter : ").upper()
        #print('____________________________________________________________')
        if guess in correct or guess in incorrect:
            print("you have already guessed that letter. Guess Again !!")
        elif guess.isnumeric():
            print("please enter only letters. Guess Again !!")
        elif len(guess) > 1:
            print("please guess only one letter at a time. Guess Again !! ")
        elif len(guess) == 0:
            print("please enter ur selection.")
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
            return 'no win'
    return 'win'

while True:
    draw_board()
    user_guess()
    
    win_condition = check_win()
    if win_condition == 'loss':
        print("\n******************************************")
        print(hangman_board[6])
        print("\nGAME OVER :(")
        print("The correct word was '" , secret_word ,"' ")
        print("******************************************")
        break
    elif win_condition == 'win':
        print("\n******************************************")
        print(" VICTORY :) ")
        print("******************************************")
        break
    
