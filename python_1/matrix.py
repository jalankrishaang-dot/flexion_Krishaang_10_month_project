
# Matrix Digital Rain
# A beginner-friendly Python animation

import random
import string
import time
import os

# Screen settings
width = 60
height = 20

# Characters used in the animation
characters = string.ascii_letters + string.digits + string.punctuation

# Starting position of each falling character
drops = [random.randint(-height, 0) for _ in range(width)]

try:
    while True:
        # Create an empty screen
        screen = [[" " for _ in range(width)] for _ in range(height)]

        # Update each column
        for x in range(width):
            y = drops[x]

            # Draw the character if it is on screen
            if 0 <= y < height:
                screen[y][x] = random.choice(characters)

            # Move the character down
            drops[x] += 1

            # Restart at the top when it reaches the bottom
            if drops[x] >= height:
                drops[x] = random.randint(-10, 0)

        # Clear the terminal and move the cursor to the top
        print("\033[2J\033[H", end="")

        # Display the animation in green
        print("\033[32m", end="")

        for row in screen:
            print("".join(row))

        # Reset terminal color
        print("\033[0m", end="")

        # Control animation speed
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\033[0m")
    print("\nMatrix animation stopped.")
