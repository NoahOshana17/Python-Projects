import random
from words import word_list
from hangmanGUI import hangmanUI


def create_random_word():
    word = random.choice(word_list)
    return word


def game_intro():
    result = False
    player_input = input("Hello and Welcome to Hangman!" + "\nTo play a game of Hangman, type 'y'. If you would like "
                                                           "to exit, type 'n': ")
    if player_input == 'y' or player_input == 'Y':
        result = True
    elif player_input == 'n' or player_input == 'N':
        print("Maybe next time")
    else:
        print("invalid input")

    return result



def start_game():
    word = create_random_word()
    word_progress = "_" * len(word)
    guessed_letters = []
    guessed_words = []
    guess_count = 0
    player_tries_left = 6

    print(hangmanUI[player_tries_left])
    print(word_progress)
    print(word)
    while player_tries_left > 0:
        player_guess = input("Guess a letter: ")
        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in guessed_letters:
                print("you have already guessed that letter")
            elif player_guess in word:
                print("correct")
                guess_count += 1
                guessed_letters.append(player_guess)
            else:
                player_tries_left -= 1
                print(hangmanUI[player_tries_left])
                guess_count += 1
                guessed_letters.append(player_guess)
                if player_tries_left == 0:
                    print("game over")
        else:
            if player_guess == word:
                guess_count += 1
                print("Correct! The word was " + word + "!" + "\nIt took you " + str(guess_count) + " trie(s) to guess "
                                                                                                    "the word.")
                break

            else:
                print("Incorrect. " + player_guess + " is not the word...")
                player_tries_left -= 1
                guess_count += 1
                print(hangmanUI[player_tries_left])


if game_intro():
    start_game()
else:
    print("User has exited game")


#maybe make a play game function that initiates when player input calls function
#Testing git clone on laptop part 2
