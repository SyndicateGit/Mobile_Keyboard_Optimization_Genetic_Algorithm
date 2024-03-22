from KeyboardObject import Keyboard
import KeySwap
import GUI
import Evaluate

# Main is where we do the scripting for the pipeline and generate the
# list of keyboards representing the top performing keyboard of a generation
# to pass to GUI for display.
import sys
sys.path.append('..')


import csv

text_data = "marryhadalittlelamb.123"

max_rows = 100  # The file is very big, so we should choose a max_rows to be read from the data

# Openning the Data file and only storing 
# relevant information in the text_data variable.
# TODO: csv_reader had unicode decoder error. 
with open("the-reddit-dataset-dataset-comments.csv", "r") as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)
    
    for i, row in enumerate(csv_reader):
        if "[deleted]" in row["body"]:
            continue
        elif "[removed]" in row["body"]:
            continue
        elif "I am a bot" in row["body"]:
            continue
        # Removing any posts with links because they include many
        # special characters that would usually not be types by the user.
        elif "https://" in row["body"]:
            continue
        elif "&amp" in row["body"]:
            continue
        elif "http://" in row["body"]:
            continue
        elif "[website]" in row["body"]:
            continue
        
        text_data += row["body"]
        
        if i + 1 >= max_rows:
            break 

def generate_initial_keyboards():
    # Generate a list of keyboards
    keyboards = []
    for i in range(100):
        keyboard = Keyboard()
        keyboard.randomize_keys()
        keyboards.append(keyboard)
    return keyboards

def evaluate_keyboards(keyboards, text_data):
    # Evaluate each keyboard
    for keyboard in keyboards:
        Evaluate.evaluate_keyboard(keyboard, text_data)

def select_top_performing_keyboards(keyboards, n):
    return