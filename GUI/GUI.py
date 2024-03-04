from Mobile_Keyboard_Optimization_Genetic_Algorithm.Main.KeyboardObject import Keyboard

# Graphics of keyboard and performance graphs.
# For now, we just want to display the best performing keyboard on screen.
# We'll also display its performance evaluation score.
# Later on we'll display pretty graphs showing how the keyboard
# performs over x generations.
# We'll be able to click left or right to view the next or previous generation by
# rendering a list of keyboards.

# Probably pyturtle for graphics but whoever in charge can decide.
# Here's the documentation:
# https://docs.python.org/3/library/turtle.html
# Make sure to update Read.me with any installation dependencies like
# from turtle import * in commandline

# I'm not too sure how pyturtle works for making graphics works. You may need
# to have other functions that call these functions to update screen. However,
# we are running all our functions in main through imports, so make sure there aren't
# global variables, just functions. Main itself can have pyturtle installed.

# Displays keyboard layout on screen.
# Parameter Type: keyboard object
# Dependencies: KeyboardObject.py
def display_keyboard(keyboard):
    return

# Keyboard object have attributes for performance scores that will
# be display on screen.
# Parameter Type: keyboard object
# Dependencies: KeyboardObject.py
def display_keyboard_performance_score(keyboard):
    return

# Fetch a list of keyboard objects ordered by generation. Display a screen
# with keyboard and performance evaluation score. While in screen, able to click
# left or right for traversing the keyboard list (1st generation to n generation).
# Parameter Type: [keyboard object...]
# Dependencies: KeyboardObject.py, display_keyboard, display_keyboard_performance_score
def display_keyboards(keyboards):
    return
