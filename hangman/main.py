import random
from words import word_list
from hangmanGUI import hangmanUI


def createRandomWord():
    word = random.choice(word_list)
    return word


word = createRandomWord()
print(word)

player_tries = 0
incorrect_guess_count = 0

while incorrect_guess_count < 7:
    print(hangmanUI[incorrect_guess_count])
    player_input = input("Guess a letter")
    if player_input in word:
        print("correct")
        player_tries += 1
    else:
        print(hangmanUI[incorrect_guess_count])
        incorrect_guess_count += 1
        player_tries += 1
        if incorrect_guess_count == 6:
            print("game over")


#maybe make a play game function that initiates when player input calls function
