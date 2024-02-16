# Keyboard Object
class Keyboard:
    # Coordinates of all keys representing (x,y) coordinate
    # (0,0) starts at bottom right of screen for right hand mode
    # Hard coded values depending on initial layout design based on
    # Thumbly layout.
    # Type: Dict{key: value}
    # Key Type: int (1 to 47)
    # Value Type: tuple(x, y)
    key_coordinates = {}
    # Assignment of keys
    key_assignment = {}

    # Randomize key assignments
    def randomize_keys(self):
        return

    # Calculates distance between 2 keys using euclidian distance
    # Param type: string. Example: calc_distance("A", "B")
    # Return type: float Example: 2.52
    def calc_distance(self, key1, key2):
        return