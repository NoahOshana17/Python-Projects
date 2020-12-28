import random
from tkinter import *
from words import word_list
from hangmanGUI import hangmanUI


# Pulls random word from the words module
def create_random_word():
    word = random.choice(word_list)
    return word


# Prompts the user to decide to play or exit
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


# Hangman game play
def start_game():
    game_result = False

    word = create_random_word()
    guessed_letters = []
    guessed_words = []
    guess_count = 0
    player_tries_left = 6
    letters_in_word = set(word)

    while len(letters_in_word) > 0 and player_tries_left > 0:

        word_progress = [letter if letter in guessed_letters else '_' for letter in word]
        word_progress_format = ' '.join(word_progress)

        print(hangmanUI[player_tries_left])
        print(word_progress_format)
        player_guess = input("Guess a letter: ")
        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in guessed_letters:
                print("you have already guessed that letter")

            elif player_guess in word:
                print("correct")
                guess_count += 1
                guessed_letters.append(player_guess)
                letters_in_word.pop()

            else:
                player_tries_left -= 1
                guess_count += 1
                guessed_letters.append(player_guess)

        else:
            if player_guess == word:
                guess_count += 1
                print("Correct! The word was " + word + "!" + "\nIt took you " + str(guess_count) + " tries to guess "
                                                                                                    "the word.")
                guessed_words.append(player_guess)
                game_result = True
                break

            else:
                print("Incorrect. " + player_guess + " is not the word...")
                player_tries_left -= 1
                guess_count += 1
                guessed_words.append(player_guess)
                print(hangmanUI[player_tries_left])


# checking if use wants to play or not
# if game_intro():
#     start_game()
# else:
#     print("User has exited game")

# maybe make a play game function that initiates when player input calls function
# Testing git clone on laptop part 2


# Creating GUI using tkinter
# Creating window and title for hangman
window = Tk()
window.title("Hangman")
# Sets dimensions of window
window.geometry("400x400")
# Creating label
label = Label(window, text="Welcome To Hangman!", fg="black", bg="green")
label.pack()

# Creating button to begin game
begin_button = Button(window, text="Play", command=start_game)
begin_button.pack()
window.mainloop()