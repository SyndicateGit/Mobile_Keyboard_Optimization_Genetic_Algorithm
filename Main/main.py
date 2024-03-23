from KeyboardObject import Keyboard
import KeySwap
import GUI
import Evaluate
from random import randrange

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
len_data = len(text_data)
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
    return

def sort_keyboards_by_combined_score(keyboards):
  keyboards.sort(key=lambda x: x.combined_score, reverse=True)
  # for keyboard in keyboards:
  #   print(keyboard.combined_score)
  return

def select_top_performing_keyboards(keyboards, n):
  sort_keyboards_by_combined_score(keyboards)
  return keyboards[:n]

def generate_next_generation(keyboards, n):
  next_generation = []
  for i in range(n - 10):
    parent1_index = randrange(0, 10)
    parent2_index = randrange(0, 10)
    while(parent1_index == parent2_index):
      parent2_index = randrange(0, 10)
      #TODO: Fix error
    # Error is here... appending new keyboard object somehow references the same object for all.
    # This makes it so any old child of next_generation is the same as the new child.
    child = Keyboard()
    child = KeySwap.key_swap(keyboards[parent1_index], keyboards[parent2_index])
    next_generation.append(child)
    
    
  for i in range(len(next_generation)):
    # Different object reference for each child
    print("Child number: ", i)
    print(next_generation[i].key_assignment)
    
  for keyboard in keyboards:
    next_generation.append(keyboard)
  
  return next_generation
  
def printKeyboardScores(keyboards):
  for keyboard in keyboards:
    print(keyboard.combined_score)
  return

def main():
  # Default QWERTY Keyboard
  Bob = Keyboard()
  Evaluate.evaluate_keyboard(Bob, text_data)
  target_score = Bob.combined_score
  print("Target Score:", target_score)
  
  current_score = 0
  generation = 1
  keyboards = generate_initial_keyboards()

  #while(current_score < target_score * 1.5):
  evaluate_keyboards(keyboards, text_data)
  sort_keyboards_by_combined_score(keyboards)
  keyboards = keyboards[:10]
  current_score = keyboards[0].combined_score
  print("Generation " + str(generation) + " Score:", current_score)
  generate_next_generation(keyboards, 50)
    
  generation += 1
    
  

main()