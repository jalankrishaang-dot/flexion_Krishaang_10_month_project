\
# This is the start of my stickman game
# Everyone starts with nothing and has 6 chances to get to the end of the game.
# If you fail, you lose. If you succeed, you win.

import random

player_name = "new player"
number_of_chances = 6
number_of_right_letters = 0

name = input("What is your name? ")
if name:
    player_name = name
    print("Welcome to the game, " + player_name + "! You have " + str(number_of_chances) + " chances to win.")

pick = random.choice(["arise", "stare", "audio", "baker", "cable", "dance", "eagle", "fable", "gamer", "hiker"])
selected_word = pick

if selected_word:
    print("The word has been selected. It has " + str(len(selected_word)) + " letters.")
    print("You have " + str(number_of_chances) + " chances to guess the word.")

chance = input("Guess the first letter of the word: ")

if chance:
    if chance in selected_word:
        number_of_right_letters += 1
        print("Good job! You have guessed " + str(number_of_right_letters) + " letters correctly.")
    else:
        number_of_chances -= 1
        print("Sorry, that letter is not in the word. You have " + str(number_of_chances) + " chances left.")

# This is the part where the player can choose to see where the letter is in the word

show_where = input("Do you want to see where the letter is in the word? (yes/no) ")
if show_where.strip().lower() == "yes":
    positions = [i for i, letter in enumerate(selected_word, start=1) if letter == chance]
    print("The letter " + chance + " is in the following positions: " + str(positions))

repeat = input("Do you want to guess another letter? (yes/no) ")
if repeat.strip().lower() == "no":
    print("Thank you for playing, " + player_name + "!")
    print("The word was '" + selected_word + "'. Better luck next time!")

if repeat.strip().lower() == "yes":
    while number_of_chances > 0 and number_of_right_letters < len(selected_word):
        chance = input("Guess another letter: ")
        if chance in selected_word:
            number_of_right_letters += 1
            print("Good job! You have guessed " + str(number_of_right_letters) + " letters correctly.")
        else:
            number_of_chances -= 1
            print("Sorry, that letter is not in the word. You have " + str(number_of_chances) + " chances left.")

        show_where = input("Do you want to see where the letter is in the word? (yes/no) ")
        if show_where.strip().lower() == "yes":
            positions = [i for i, letter in enumerate(selected_word, start=1) if letter == chance]
            print("The letter " + chance + " is in the following positions: " + str(positions))

if number_of_right_letters == len(selected_word):
    print("Congratulations, " + player_name + "! You have guessed the word correctly and won the game!")

if number_of_chances == 0:
    finnal_chance = input("You have run out of chances. Do you want to try again? (yes/no) ").strip().lower()
    if finnal_chance == "yes":
        let_user_guess_the_full_word = input("Please guess the full word: ").strip().lower()
        if let_user_guess_the_full_word == selected_word:
            print("Congratulations, " + player_name + "! You have guessed the word correctly and won the game!")
        else:
            print("Sorry, " + player_name + ". The word was '" + selected_word + "'. Better luck next time!")
    else:
        print("The word was '" + selected_word + "'. Better luck next time!")
        print("Thank you for playing, " + player_name + "!")
        retry = input("Do you want to play again? (yes/no) ").strip().lower()
        if retry == "yes":
            # Reset game state
            number_of_chances = 6
            number_of_right_letters = 0
            selected_word = random.choice(["arise", "stare", "audio", "baker", "cable", "dance", "eagle", "fable", "gamer", "hiker"])
            print("A new word has been selected. It has " + str(len(selected_word)) + " letters.")
            print("You have " + str(number_of_chances) + " chances to guess the word.")

# The game was just my project for semester 1
# Thank you for playing my game. I hope you enjoyed it!
