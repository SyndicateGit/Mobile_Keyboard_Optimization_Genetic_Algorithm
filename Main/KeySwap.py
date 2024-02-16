import KeyboardObject

# Key swap algorithm
# Returns new keyboard object with half of
# its keys from parent 1 and half of its keys from
# parent 2 based on algorithm described in
# http://azariaa.com/Content/Publications/Keyboard_Journal.pdf
# Dependencies: KeyboardObject
# Param type: Keyboard
# Return type: Keyboard
def key_swap(keyboard1, keyboard2):
    return