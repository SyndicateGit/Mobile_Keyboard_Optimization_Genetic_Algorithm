# Keyboard Object
import random
class Keyboard:
    # Coordinates of all keys representing (x,y) coordinate
    # (0,0) starts at bottom right of screen for right hand mode
    # Hard coded values depending on initial layout design based on
    # Thumbly layout.
    # Type: Dict{key: value}
    # Key Type: int (1 to 81)
    # Value Type: tuple(x, y)
    key_coordinates = {
        1: (882,169),     #1st row LOWERCASE
        2: (847,276),
        3: (792,374),
        4: (725,464),
        5: (644,548),
        6: (545,618),
        7: (440,676),
        8: (326,721),
        9: (203,753),
        10: (77,768),
        11: (750,61),     #2nd row
        12: (727,169),
        13: (684,276),
        14: (619,369),
        15: (534,452),
        16: (439,524),
        17: (326,581),
        18: (204,619),
        19: (74,640),
        20: (597,60),     #3rd row
        21: (569,169),
        22: (508,272),
        23: (428,352),
        24: (326,433),
        25: (205,482),
        26: (76,508),
        27: (882,169),    #1st row UPPERCASE
        28: (847,276),
        29: (792,374),
        30: (725,464),
        31: (644,548),
        32: (545,618),
        33: (440,676),
        34: (326,721),
        35: (203,753),
        36: (77,768),
        37: (750,61),     #2nd row
        38: (727,169),
        39: (684,276),
        40: (619,369),
        41: (534,452),
        42: (439,524),
        43: (326,581),
        44: (204,619),
        45: (74,640),
        46: (597,60),     #3rd row
        47: (569,169),
        48: (508,272),
        49: (428,352),
        50: (326,433),
        51: (205,482),
        52: (76,508),
        53: (882,169),    #1st row NUMBERS & SYMBOLS
        54: (847,276),
        55: (792,374),
        56: (725,464),
        57: (644,548),
        58: (545,618),
        59: (440,676),
        60: (326,721),
        61: (203,753),
        62: (77,768),
        63: (750,61),     #2nd row
        64: (727,169),
        65: (684,276),
        66: (619,369),
        67: (534,452),
        68: (439,524),
        69: (326,581),
        70: (204,619),
        71: (74,640),
        72: (597,60),     #3rd row
        73: (569,169),
        74: (508,272),
        75: (428,352),
        76: (326,433),
        77: (205,482),
        78: (76,508),
        79: (280,205),    #space
        80: (447,46),     #shift
        81: (63,366)      #123/abc
    }  # TODO: Michael
    # Assignment of keys
    # Key Type: String(), example: 'A'
    # Value: int (1 to 81)
    # TODO: Delete capital letters from all three dictionaries.
    #  Since we're making capital letters match lower case letter location... we don't
    #  need key assignment for capital letters. We can just have the shift key make all the characters
    #  on screen alternate between cases.
    #  This also makes KeySwap easier for me logic wise.
    key_assignment = {
        "q": 1,             #LOWERCASE
        "w": 2,
        "e": 3,
        "r": 4,
        "t": 5,
        "y": 6,
        "u": 7,
        "i": 8,
        "o": 9,
        "p": 10,
        "a": 11,
        "s": 12,
        "d": 13,
        "f": 14,
        "g": 15,
        "h": 16,
        "j": 17,
        "k": 18,
        "l": 19,
        "z": 20,
        "x": 21,
        "c": 22,
        "v": 23,
        "b": 24,
        "n": 25,
        "m": 26,
        # "Q": 27,            #UPPERCASE
        # "W": 28,
        # "E": 29,
        # "R": 30,
        # "T": 31,
        # "Y": 32,
        # "U": 33,
        # "I": 34,
        # "O": 35,
        # "P": 36,
        # "A": 37,
        # "S": 38,
        # "D": 39,
        # "F": 40,
        # "G": 41,
        # "H": 42,
        # "J": 43,
        # "K": 44,
        # "L": 45,
        # "Z": 46,
        # "X": 47,
        # "C": 48,
        # "V": 49,
        # "B": 50,
        # "N": 51,
        # "M": 52,
        "1": 53,            #NUMBERS & SYMBOLS
        "2": 54,
        "3": 55,
        "4": 56,
        "5": 57,
        "6": 58,
        "7": 59,
        "8": 60,
        "9": 61,
        "0": 62,
        "-": 63,
        "/": 64,
        ":": 65,
        ";": 66,
        "(": 67,
        ")": 68,
        "$": 69,
        "&": 70,
        "@": 71,
        "QUOTATION": 72,
        ".": 73,
        ",": 74,
        "?": 75,
        "!": 76,
        "'": 77,
        "+": 78,
        "SPACE": 79,
        "SHIFT": 80,        #SPECIAL/KEYBOARD CHANGING CHARACTERS (EX: Keyb1: 1-26, Keyb2: 27-52, Keyb3: 53-78... 79, 80, and 81 Static)
        "123": 81
    }  # TODO: Michael default qwerty
    # Comfortability scores
    # Key Type: int (1 to 81)
    # Value: int (comfort score decided based on ergonomics paper) - scale of 1 to 10.
    key_comfort = {
        "1": 9,     #1st row LOWERCASE
        "2": 9,
        "3": 9,
        "4": 9,
        "5": 9,
        "6": 9,
        "7": 9,
        "8": 9,
        "9": 9,
        "10": 8,
        "11": 9,     #2nd row
        "12": 9,
        "13": 10,
        "14": 10,
        "15": 10,
        "16": 10,
        "17": 10,
        "18": 10,
        "19": 9,
        "20": 9,     #3rd row
        "21": 10,
        "22": 10,
        "23": 10,
        "24": 9,
        "25": 8,
        "26": 7,
        "27": 9,    #1st row UPPERCASE
        "28": 9,
        "29": 9,
        "30": 9,
        "31": 9,
        "32": 9,
        "33": 9,
        "34": 9,
        "35": 9,
        "36": 8,
        "37": 9,     #2nd row
        "38": 9,
        "39": 10,
        "40": 10,
        "41": 10,
        "42": 10,
        "43": 10,
        "44": 10,
        "45": 9,
        "46": 9,     #3rd row
        "47": 10,
        "48": 10,
        "49": 10,
        "50": 9,
        "51": 8,
        "52": 7,
        "53": 9,    #1st row NUMBERS & SYMBOLS
        "54": 9,
        "55": 9,
        "56": 9,
        "57": 9,
        "58": 9,
        "59": 9,
        "60": 9,
        "61": 9,
        "62": 8,
        "63": 9,     #2nd row
        "64": 9,
        "65": 10,
        "66": 10,
        "67": 10,
        "68": 10,
        "69": 10,
        "70": 10,
        "71": 9,
        "72": 9,     #3rd row
        "73": 10,
        "74": 10,
        "75": 10,
        "76": 9,
        "77": 8,
        "78": 7,
        "79": 7,    #space
        "80": 8,     #shift
        "81": 6      #123/abc
    }  # TODO: Sal, look into ergo paper.

    key_assignment_letters = {
        "q": 1,  # LOWERCASE
        "w": 2,
        "e": 3,
        "r": 4,
        "t": 5,
        "y": 6,
        "u": 7,
        "i": 8,
        "o": 9,
        "p": 10,
        "a": 11,
        "s": 12,
        "d": 13,
        "f": 14,
        "g": 15,
        "h": 16,
        "j": 17,
        "k": 18,
        "l": 19,
        "z": 20,
        "x": 21,
        "c": 22,
        "v": 23,
        "b": 24,
        "n": 25,
        "m": 26,
    }

    key_assignment_non_letters = {
        "1": 53,  # NUMBERS & SYMBOLS
        "2": 54,
        "3": 55,
        "4": 56,
        "5": 57,
        "6": 58,
        "7": 59,
        "8": 60,
        "9": 61,
        "0": 62,
        "-": 63,
        "/": 64,
        ":": 65,
        ";": 66,
        "(": 67,
        ")": 68,
        "$": 69,
        "&": 70,
        "@": 71,
        "QUOTATION": 72,
        ".": 73,
        ",": 74,
        "?": 75,
        "!": 76,
        "'": 77,
        "+": 78,
    }

    key_assignment_statics = {
        "SPACE": 79,
        "SHIFT": 80,
        # SPECIAL/KEYBOARD CHANGING CHARACTERS (EX: Keyb1: 1-26, Keyb2: 27-52, Keyb3: 53-78... 79, 80, and 81 Static)
        "123": 81
    }
    # Performance scores to be evaluated
    comfort_score: 0
    total_distance_traveled: 0

    # Randomize key assignments
    # In key_assignment dictionary, randomizly swap the values between letter groups.
    # Do the same for non letter group.
    # No parameter, working with self key_assignment field.
    # Return: None. Mutating key_assignment field.
    def randomize_keys(self):  # TODO: Azwad
        # TODO: We don't want to shuffle letter keys with special keys for key assignment
        #   Shuffle letter key assignments
        #   Then shuffle special key assignments.
        #   We don't want SPACE, SHIFT, and 123/ABC key shuffled.
        # Extract the keys and values from the key_assignment dictionary
        keys_letters = list(self.key_assignment_letters.keys())
        values_letters = list(self.key_assignment_letters.values())

        keys_non_letters = list(self.key_assignment_non_letters.keys())
        values_non_letters = list(self.key_assignment_non_letters.values())

        # Shuffle the values randomly
        random.shuffle(values_letters)
        random.shuffle(values_non_letters)
        
        # Update the key_assignment dictionary with the shuffled values
        self.key_assignment_letters = dict(zip(keys_letters, values_letters))
        self.key_assignment_non_letters = dict(zip(keys_non_letters, values_non_letters))
        self.key_assignment = self.key_assignment_letters | self.key_assignment_non_letters | self.key_assignment_statics
        
    # Calculates distance between 2 keys using euclidian distance
    # Param type: string. Example: calc_distance("A", "B")
    # Return type: float Example: 2.52
    def calc_distance(self, key1, key2):  # TODO: Jasmine
        # Retrieve the integer codes for the keys
        key1_code = self.key_assignment[key1]
        key2_code = self.key_assignment[key2]

        # Retrieve the (x, y) coordinates for the keys
        key1_coordinates = self.key_coordinates[str(key1_code)]
        key2_coordinates = self.key_coordinates[str(key2_code)]

        # Calculate the Euclidean distance
        distance = ((key2_coordinates[0] - key1_coordinates[0])**2 + (key2_coordinates[1] - key1_coordinates[1])**2)**0.5
        # d = Δx^2 + Δy^2
        return distance


# Testing
# randomize_key
test_keyboard = Keyboard()
test_keyboard.randomize_keys()
print(test_keyboard.key_assignment)

