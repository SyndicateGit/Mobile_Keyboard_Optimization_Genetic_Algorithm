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
    # Start a cycle:
    # Pop a key from the list and assign the key location in object
    # to the location where that key is in keyboard 1.
    # Find out which key gets displaced for keyboard 2 in key assignment.
    # That displaced key becomes the next key to be assigned using keyboard 1.
    # This cycle continues until we go back to the first key that got assigned.
    # ^This is if detection at beginning of loop
    # End of a cycle
    # Every key assigned thus far would be from keyboard 1.
    # Next pop another key from list and continue but this time with keyboard 2.

    return

# Mutation
# Randomly swap n keys.
# Take n random keys from the key assignment list, randomize the keys.
# Param type: keyboard object
# Return type: keyboard object
def mutate(keyboard, n):
    return


# Test Keyboards:
keyboard1 = Keyboard()
keyboard2 = Keyboard()

# Testing KeySwap:
key_swap(keyboard1, keyboard2)
