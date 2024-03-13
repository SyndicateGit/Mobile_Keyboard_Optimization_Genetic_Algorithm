from KeyboardObject import Keyboard
import random

# Key swap algorithm
# Returns new keyboard object with half of
# its keys from parent 1 and half of its keys from
# parent 2 based on algorithm described in
# http://azariaa.com/Content/Publications/Keyboard_Journal.pdf
# Described on page 4 left paragraph
# Dependencies: KeyboardObject.py
# Param type: Keyboard object
# Return type: Keyboard object
# Things to keep in mind: Lowercase and Uppercase same location.
# Keep spaces, shift, and 123 key locked.
def key_swap(keyboard1, keyboard2):
    # Create new keyboard object for child keyboard to be returned
    child_keyboard = Keyboard()

    # Have a list of all assignable characters (excluding Capital cases)
    # Randomize that list
    assignable_characters = list(child_keyboard.key_assignment.keys())
    assignable_characters = [key for key in assignable_characters if (len(key) > 1 or not key.isupper())]
    random.shuffle(assignable_characters)

    # While the assignable list still has assignable characters:
    while(assignable_characters):
        # Start a cycle:
        # Pop a key from the list and assign the key location in child keyboard
        # to the key of a random parent (this parent becomes parent_assign_keyboard)
        # Find out which key gets displaced from the other keyboard that becomes parent_displaced_keyboard.
        # That displaced key becomes the next key to be assigned using parent_assign_keyboard.
        # This cycle continues until we go back to the first key that got assigned.
        # ^This is if detection at beginning of loop
        # End of a cycle
        # Every key assigned in a cycle would be from one keyboard.
        # Next pop another key from list and continue.
        cycle_start_key = assignable_characters.pop()
        current_key = cycle_start_key
        key_displaced = -1
        selected_parent = random.choice([1, 2])
        while key_displaced != cycle_start_key:
            if(selected_parent == 1):
                parent_assign_keyboard = keyboard1
                parent_displaced_keyboard = keyboard2
            else:
                parent_assign_keyboard = keyboard2
                parent_displaced_keyboard = keyboard1

            key_being_assigned = parent_assign_keyboard.key_assignment[current_key]
            child_keyboard.key_assignment[current_key] = key_being_assigned
            key_displaced = find_key_by_value(parent_displaced_keyboard, key_being_assigned)

            if(key_displaced == cycle_start_key):  # Both parents have same location for key assigned
                continue

            assignable_characters.remove(key_displaced)
            current_key = key_displaced

    return child_keyboard

# Helper function that searches for key assigned to key number on keyboard
def find_key_by_value(keyboard, key_number):
    for key, value in keyboard.key_assignment.items():
        if value == key_number:
            return key
# Mutation
# Randomly swap n keys.
# Take n random keys from the key assignment list, randomize the keys.
# Param type: keyboard object
# Return type: keyboard object
def mutate(keyboard, n):
    # Have a list of all key assignment list (excluding Capital cases)
    # Populating that list
    assignable_characters = list(keyboard.key_assignment.keys())
    assignable_characters = [key for key in assignable_characters if (len(key) > 1 or not key.isupper())]

    # Take n random keys from the assignable characters list and shuffle
    mutate_keys = random.sample(assignable_characters, min(n, len(assignable_characters)))
    random.shuffle(mutate_keys)

    # Reassigning shuffled keys to the keyboard to then be returned
    for key in mutate_keys:
        # Obtaining key number for current key
        keyNumber = keyboard.key_assignment[key]

        # Removing key from its current spot
        del keyboard.key_assignment[key]

        # Assign the key to a random location
        newKey = random.choice(assignable_characters)
        keyboard.key_assignment[newKey] = keyNumber
        
        #Remove the new key from assignable_characters list
        assignable_characters.remove(newKey)

    return keyboard


# Test Keyboards:
keyboard1 = Keyboard()
keyboard1.randomize_keys()
keyboard2 = Keyboard()
keyboard2.randomize_keys()

# Testing KeySwap:
print("Keyboard1 : ")
print(keyboard1.key_assignment)
print("Keyboard2 : ")
print(keyboard2.key_assignment)
print("Child Keyboard: ")
print(key_swap(keyboard1, keyboard2).key_assignment)
