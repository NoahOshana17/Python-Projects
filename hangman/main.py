import random
from words import word_list
from hangmanGUI import hangmanUI


def create_random_word():
    word = random.choice(word_list)
    return word


def game_intro():
    player_input = input("Hello and Welcome to Hangman!" + "\nTo play a game of Hangman, type 'y'. If you would like "
                                                           "to exit, type 'n': ")
    if player_input == 'y' or 'Y':
        return True
    elif player_input == 'n' or 'N':
        return False
    else:
        print("invalid input")


    def update_word(word):
        length = len(word)



def start_game():
    word = create_random_word()
    guess_count = 0
    player_tries_left = 6

    print(hangmanUI[player_tries_left])
    while player_tries_left > 0:
        player_input = input("Guess a letter: ")
        if player_input in word:
            print("correct")
            guess_count += 1
        else:
            player_tries_left -= 1
            print(hangmanUI[player_tries_left])
            guess_count += 1
            if player_tries_left == 0:
                print("game over")

if game_intro():
    start_game()
else:
    print("User has exited game")




#maybe make a play game function that initiates when player input calls function
