from KeyboardObject import Keyboard
import KeySwap
import GUI
import Evaluate
import random

import matplotlib.pyplot as plt

# Main is where we do the scripting for the pipeline and generate the
# list of keyboards representing the top performing keyboard of a generation
# to pass to GUI for display.
import sys
sys.path.append('..')
parentIndex1 = 0
parentIndex2 = 0

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

def generate_next_generation(keyboards, n, seed):
  next_generation = []
  for i in range(n - 20):
    random.seed(random.randint(0, seed**2 + i))
    parentIndex1 = random.randint(0, 9)
    parentIndex2 = random.randint(0, 9)
    while(parentIndex1 == parentIndex2):
      parentIndex2 = random.randint(0, 9)

    child = Keyboard()
    child = KeySwap.key_swap(keyboards[parentIndex1], keyboards[parentIndex2])
    child = KeySwap.mutate(child, 3)
    next_generation.append(child)
    
  for keyboard in keyboards:
    next_generation.append(keyboard)
  
  for i in range(10):
    keyboard = Keyboard()
    keyboard.randomize_keys()
    next_generation.append(keyboard)
    
  return next_generation
  
  
def printKeyboardScores(keyboards):
  for keyboard in keyboards:
    print(keyboard.combined_score)
  return

def printKeyboardKeys(keyboards):
  for keyboard in keyboards:
    print(keyboard.key_assignment)
  return

def main():
  # Default QWERTY Keyboard
  Bob = Keyboard()
  Evaluate.evaluate_keyboard(Bob, text_data)
  target_score = Bob.combined_score
  target_total_distance_traveled = Bob.total_distance_traveled
  target_total_comfort_score = Bob.comfort_score
  print("QWERTY Score:", target_score)
  print("Target Score:", target_score * 1.50)
  
  combined_score_plot = []
  total_distance_traveled_plot = []
  total_comfort_score_plot = []
  
  current_score = 0
  generation = 1
  keyboards = generate_initial_keyboards()
  while(current_score < target_score *1.5 and generation < 50):
    evaluate_keyboards(keyboards, text_data)
    sort_keyboards_by_combined_score(keyboards)
    keyboards = keyboards[:10]
    current_score = keyboards[0].combined_score
    current_total_distance_traveled = keyboards[0].total_distance_traveled
    current_total_comfort_score = keyboards[0].comfort_score
    print("Generation " + str(generation) + " Normalized Score (relative to QWERTY Score):", current_score/target_score)
    combined_score_plot.append((generation, current_score/target_score))
    total_comfort_score_plot.append((generation, current_total_comfort_score/target_total_comfort_score))
    total_distance_traveled_plot.append((generation, current_total_distance_traveled/target_total_distance_traveled))
    # This is needed for the next random part to work, not sure why
    random.shuffle(keyboards)
    keyboards = generate_next_generation(keyboards, 100, generation)
    generation += 1
    
  plt.scatter(*zip(*combined_score_plot))
  plt.title("Normalized Score of Top Keyboard per Generation")
  plt.xlabel("Generation")
  plt.ylabel("Normalized Score (QWERTY = 1)")
  plt.show()
  
  plt.scatter(*zip(*total_comfort_score_plot))
  plt.title("Total Comfort Score of Top Keyboard per Generation")
  plt.xlabel("Generation")
  plt.ylabel("Total Comfort Score")
  plt.show()
  
  plt.scatter(*zip(*total_distance_traveled_plot))
  plt.title("Total Distance Traveled of Top Keyboard per Generation")
  plt.xlabel("Generation")
  plt.ylabel("Total Distance Traveled")
  plt.show()
  
  GUI.display_mirrored_keys_with_horizontal_flip(keyboards[0])

main()