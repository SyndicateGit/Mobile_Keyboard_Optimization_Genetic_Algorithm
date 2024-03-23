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
def display_mirrored_keys_with_horizontal_flip(keyboard):
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Mirrored Keyboard Layout with Horizontal Flip")

    pen = turtle.Turtle()
    pen.penup()
    pen.speed(0)

    key_width = 50
    key_height = 50

    # For making the key_assignments map number to character, rather than character to number
    inv_map = {v: k for k, v in keyboard.key_assignment.items()}

    for key, (x, y) in keyboard.key_coordinates.items():
        if key < 27 or key > 78:
            # Calculate mirrored coordinates with horizontal flip
            mirrored_x = -x - 200
            mirrored_y = y - 350

            pen.goto(mirrored_x + 875, mirrored_y - 80)
            pen.pendown()
            pen.begin_fill()
            for _ in range(4):
                pen.forward(key_width)
                pen.right(90)
            pen.end_fill()
            pen.penup()

            pen.goto(mirrored_x + key_width / 2 + 875 + 2, mirrored_y + key_height / 2 - 80 - 58)

            pen.color("white")
            pen.write(inv_map[key].upper(), align="center", font=("Arial", 12, "normal"))
            pen.color("black")

    pen.hideturtle()

    screen.mainloop()

# Keyboard object have attributes for performance scores that will
# be displayed on screen.
# Parameter Type: keyboard object
# Dependencies: KeyboardObject.py
# def display_keyboard_performance_score(keyboard):
#     print("Performance Evaluation Score:")
#     print("Total Distance Travelled:", keyboard.total_distance_travelled)
#     print("Total Comfort Score:", keyboard.total_comfort_score)

# Function to display a keyboard and its performance score


#test_keyboard = Keyboard()
#test_keyboard.randomize_keys()

#display_mirrored_keys_with_horizontal_flip(test_keyboard)
