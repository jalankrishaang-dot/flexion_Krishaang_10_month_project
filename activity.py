# write new lines of function with python
from random import choice


def new_function():

    # This is a new function that chooses a random person from a list and prints their name
    chosen_person = input("Enter a name: ")
   
    print(chosen_person)

    # What their name has been selected for
    options = [
        "you have sucessfully been registered for the soccer game held in chicago",
        "you have been registered for the soccer game held in new york",
        "you have been registered for the soccer game held in los angeles",
        "you have been registered for the soccer game held in miami",
    ]
    print("Congratulations, " + chosen_person + ", " + choice(options) + "!")
new_function()

new_function()
print("do you want to go to this game? (yes/no)")
response = input().lower()
if response == "yes":
    print("Great! We will see you there!")
elif response == "no":
    print("No worries! Maybe next time.")
new_function()