
import random

MAX_TRIES = 6

HANGMAN_ASCII_ART = ("""                                   
Welcome to the game
  _    _ 
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
""")
print(HANGMAN_ASCII_ART)
print(MAX_TRIES)

STAGE_ONE = ("    x-------x")

STAGE_TWO = ("""    x-------x
    |
    |
    |
    |
    |""")

STAGE_THREE = ("""    x-------x
    |       |
    |       0
    |
    |
    |""")

STAGE_FOUR = ("""    x-------x
    |       |
    |       0
    |       |
    |
    |
""")

STAGE_FIVE = ("""    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""")

STAGE_SIX = ("""    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |

""")

STAGE_SEVEN = ("""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""")


first_try = input("Guess a letter: ")
print(first_try)

