from turtle import Turtle, Screen
from Mobile_Keyboard_Optimization_Genetic_Algorithm.Main.KeyboardObject import Keyboard

# Displays keyboard layout on screen.
# Parameter Type: keyboard object
# Dependencies: KeyboardObject.py
def display_keyboard(keyboard):
    # Set up the screen
    screen = Screen()
    screen.setup(width=600, height=400)
    screen.title("Keyboard Layout")

    # Initialize Turtle
    turtle = Turtle()
    turtle.penup()
    
    # Draw each key on the screen
    for key, (x, y) in keyboard.key_coordinates.items():
        turtle.goto(x, y)
        turtle.write(key)

    # Hide the turtle
    turtle.hideturtle()
    screen.mainloop()

# Displays keyboard performance score on screen.
# Parameter Type: keyboard object
# Dependencies: KeyboardObject.py
def display_keyboard_performance_score(keyboard):
    # Print the performance score
    print(f"Performance Score: {keyboard.performance_score}")

# Fetch a list of keyboard objects ordered by generation. Display a screen
# with keyboard and performance evaluation score. While in screen, able to click
# left or right for traversing the keyboard list (1st generation to n generation).
# Parameter Type: [keyboard object...]
# Dependencies: KeyboardObject.py, display_keyboard, display_keyboard_performance_score
def display_keyboards(keyboards):
    # Display each keyboard and its performance score
    for keyboard in keyboards:
        display_keyboard(keyboard)
        display_keyboard_performance_score(keyboard)
