#Thsi is the start of my stickman game
#everyone starts with nothing and has 6 chances to get to the end of the game. If you fail, you lose. If you succeed, you win.

import random


player_name = "new player"
number_of_chances = 6
number_of_right_letters = 0

name=input("What is your name? ")
if name:
    player_name = name
    print("Welcome to the game, " + player_name + "! You have " + str(number_of_chances) + " chances to win.")

pick = random.choice(["arise", "stare", "audio", "baker", "cable", "dance", "eagle", "fable", "gamer", "hiker"])
selected_word = pick

