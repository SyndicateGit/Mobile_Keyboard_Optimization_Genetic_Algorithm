#TODO: We might want to have everything from lines 3 to 30 in this code be included in main.py rather than here.

import csv

text_data = ""

max_rows = 10000  # The file is very big, so we should choose a max_rows to be read from the data

# Openning the Data file and only storing 
# relevant information in the text_data variable
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


print(text_data)

# Evaluate a keyboard's performance score by parsing through TextDatum
# and update the keyboard's attribute for each score.
# Parameter Type: keyboard object
# Return Type: None, keyboard is instead modified to have its score attributes
# updated.
def evaluate_keyboard(keyboard, text_data):
    total_distance = 0
    comfort_score = 0
    for i in range(len(text_data) - 1):
        key1, key2 = text_data[i], text_data[i+1]
        if key1 in keyboard.key_assignment and key2 in keyboard.key_assignment:
            # Calculate distance between successive keys
            distance = keyboard.calc_distance(key1, key2)
            total_distance += distance
            
            # Aggregate comfort scores
            key1_code = keyboard.key_assignment[key1]
            key2_code = keyboard.key_assignment[key2]
            comfort_score += (keyboard.key_comfort[str(key1_code)] + keyboard.key_comfort[str(key2_code)]) / 2
            
    # Update the keyboard object's attributes
    keyboard.total_distance_traveled = total_distance
    # Normalize comfort score based on the text length
    keyboard.comfort_score = comfort_score / len(text_data)
    return keyboard
