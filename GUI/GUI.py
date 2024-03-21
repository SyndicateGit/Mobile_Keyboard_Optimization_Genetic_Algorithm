import turtle
import tkinter as tk
from functools import partial
# from Mobile_Keyboard_Optimization_Genetic_Algorithm.Main.KeyboardObject import Keyboard
import random
def create_test_keyboard():
    from Mobile_Keyboard_Optimization_Genetic_Algorithm.Main.KeyboardObject import Keyboard
    
    # Create a new keyboard object
    test_keyboard = Keyboard()

    # Set some predefined attributes for testing
    test_keyboard.total_distance_travelled = 1234  # Example total distance travelled
    test_keyboard.total_comfort_score = 8  # Example total comfort score

    return test_keyboard

# Displays keyboard layout on screen.
# Parameter Type: keyboard object
# Dependencies: KeyboardObject.py
def display_keyboard_turtle(keyboard):
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
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
        # Move to the position
        pen.goto(x, y)
        
        # Draw the key
        pen.pendown()
        pen.begin_fill()
        for _ in range(4):
            pen.forward(key_width)
            pen.right(90)
        pen.end_fill()
        pen.penup()
        
        # Write the key label
        pen.goto(x + key_width / 2, y + key_height / 2)
        pen.write(key, align="center", font=("Arial", 12, "normal"))

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
def display_keyboard_gui(root, keyboard):
    # Create a new window
    window = tk.Toplevel(root)

    # Display keyboard layout
    display_keyboard_turtle(keyboard)

    # Display performance evaluation score
    label = tk.Label(window, text="Performance Evaluation Score:")
    label.pack()

    distance_label = tk.Label(window, text=f"Total Distance Travelled: {keyboard.total_distance_travelled}")
    distance_label.pack()

    comfort_label = tk.Label(window, text=f"Total Comfort Score: {keyboard.total_comfort_score}")
    comfort_label.pack()

# Function to display keyboards and allow traversal
def display_keyboards_gui(keyboards):
    root = tk.Tk()
    root.title("Keyboard Optimization")

    current_index = 0

    # Display the first keyboard
    display_keyboard_gui(root, keyboards[current_index])

    # Function to handle left arrow key press
    def prev_keyboard(event):
        nonlocal current_index
        current_index = (current_index - 1) % len(keyboards)
        display_keyboard_gui(root, keyboards[current_index])

    # Function to handle right arrow key press
    def next_keyboard(event):
        nonlocal current_index
        current_index = (current_index + 1) % len(keyboards)
        display_keyboard_gui(root, keyboards[current_index])

    # Bind left arrow key to display previous keyboard
    root.bind("<Left>", prev_keyboard)

    # Bind right arrow key to display next keyboard
    root.bind("<Right>", next_keyboard)

    root.mainloop()
