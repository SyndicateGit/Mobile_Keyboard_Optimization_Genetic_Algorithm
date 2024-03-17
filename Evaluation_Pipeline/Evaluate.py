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
        
        text_data += row["body"] + ' '
        
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
    last_key = 'SPACE'  # Start from a neutral position like SPACE for the first character

    print(f"Starting evaluation for text: {text_data}")
    
    for char in text_data:
        # Check if character is uppercase or special, requiring shift or direct access
        needs_shift = char.isupper() or char in keyboard.key_assignment_non_letters
        current_key = char.lower() if char.isupper() else char  # Normalize to lowercase for uppercase characters
        
        # Ensure the character or its lowercase version is in the key assignment
        if current_key in keyboard.key_assignment:
            if needs_shift:
                # Handle uppercase and special characters
                action = "Uppercase" if char.isupper() else "Special"
                
                if char.isupper():  # Uppercase characters require the shift key
                    if 'SHIFT' in keyboard.key_assignment:
                        distance_to_shift = keyboard.calc_distance(last_key, 'SHIFT')
                        distance_to_char = keyboard.calc_distance('SHIFT', current_key)
                        total_distance += distance_to_shift + distance_to_char
                        print(f"Processing {action} char '{char}' requiring SHIFT: Total Distance += {distance_to_shift + distance_to_char}")
                else:  # Special characters directly accessed
                    distance = keyboard.calc_distance(last_key, current_key)
                    total_distance += distance
                    print(f"Processing {action} char '{char}': Total Distance += {distance}")
                
                last_key = current_key  # Update last_key to current character for next iteration
            else:
                # Handle lowercase and directly accessible characters
                distance = keyboard.calc_distance(last_key, current_key)
                total_distance += distance
                print(f"Processing char '{char}': Total Distance += {distance}")
                last_key = current_key  # Update last_key to current character for next iteration
            
            # Calculate comfort score if the current key is valid
            char_key_code = keyboard.key_assignment[current_key]
            comfort = keyboard.key_comfort[str(char_key_code)]
            comfort_score += comfort
            print(f"Comfort score for '{char}': {comfort}")
        else:
            print(f"Character '{char}' not in keyboard assignment. Skipping...")
    
    # Normalize comfort score based on the text length
    keyboard.comfort_score = comfort_score / len(text_data)
    keyboard.total_distance_traveled = total_distance
    
    print(f"Total distance traveled: {total_distance}")
    print(f"Average comfort score: {keyboard.comfort_score}")
    
    return keyboard

