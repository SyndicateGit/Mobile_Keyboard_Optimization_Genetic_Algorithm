import turtle
import tkinter as tk
from functools import partial

import sys
sys.path.append('..')

from Main.KeyboardObject import Keyboard

# Displays keyboard layout on screen.
# Parameter Type: keyboard object
# Dependencies: KeyboardObject.py
#TODO: It is printing out keys as the key number instead of the value
# It also prints a black box for each key rather than a box surrounding
# the key value. 
# It does look like the spacing is correct between the keys but it's at the 
# top right corner of the screen rather than buttom left or right.
# It also prints overlapping keys (cause we have lowercase, uppercase
# # and special keys so it prints all three on top of each other).

# Step1) Relocate the starting point of the turtle to the bottom left corner
# Step2) Draw the keys values (not key number) inside the box (but not black box, just border if possible)
# Step3) Why don't we try drawing just the lowercase keys and static.
# Step4) We can then have the special keys be drawn next to the letter keys to
# show the user they occupy the same key space.
def display_keyboard_turtle(keyboard):
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=1200, height=1000)
    screen.title("Keyboard Layout")

    # Initialize Turtle
    pen = turtle.Turtle()
    pen.penup()
    pen.speed(0)

    # Define key size and spacing
    key_width = 50
    key_height = 50
    key_spacing = 10

    # Draw the keys
    for key, (x, y) in keyboard.key_coordinates.items():
        if key < 27 or key > 78:
            # Move to the position
            pen.goto(x-200, y-350)
            
            # Draw the key
            pen.pendown()
            pen.begin_fill()
            for _ in range(4):
                pen.forward(key_width)
                pen.right(90)
            pen.end_fill()
            pen.penup()
            
            # Write the key label
            pen.goto(x + key_width / 2 - 200, y + key_height / 2 - 350)
            pen.write(keyboard.key_symbol_to_number[key], align="center", font=("Arial", 12, "normal"))

    # Hide the pen
    pen.hideturtle()

    # Keep the window open
    screen.mainloop()

# Keyboard object have attributes for performance scores that will
# be displayed on screen.
# Parameter Type: keyboard object
# Dependencies: KeyboardObject.py
def display_keyboard_performance_score(keyboard):
    print("Performance Evaluation Score:")
    print("Total Distance Travelled:", keyboard.total_distance_travelled)
    print("Total Comfort Score:", keyboard.total_comfort_score)

# Function to display a keyboard and its performance score


test_keyboard = Keyboard()
test_keyboard.randomize_keys()

display_keyboard_turtle(test_keyboard)
