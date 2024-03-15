from Mobile_Keyboard_Optimization_Genetic_Algorithm.Main.KeyboardObject import Keyboard

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
