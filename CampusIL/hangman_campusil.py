
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

STAGE_SIX = ("""    x-------xs
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

old_letters = ['a', 'b']

def print_input(letter_guessed):   #% First  
    if word.isalpha() == False and word[1:] != "":
        print("E3")
    elif word.isalpha() == False:
        print("E2")
    elif word[1:] != "":
        print("E1")
    elif word[1:] == "":
        print(word)
        is_valid_input(word)
        #! return word
    else:
        print("Invalid Input")

def is_valid_input(letter_guessed): #% Second
    if word.isalpha() == False and word[1:] != "":
        print(False)
    elif word.isalpha() == False:
        print(False)
    elif word[1:] != "":
        print(False)
    elif word[1:] == "":
        print(True)
        check_valid_input(word, old_letters)
    else:
        print(False)

def check_valid_input(letter_guessed, old_letters_guessed): #% Third
    if letter_guessed not in old_letters_guessed:
        return True
    else:
        return False
 
def try_update_letter_guessed(letter_guessed, old_letters_guessed): #% Forth
    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        global old_letters
        old_letters += word
        return True
    else:
        new_list = " -> ".join(old_letters)
        print("X\n" + new_list)
        return False


word = input("Please enter a word: ").lower()
word = word.replace(" ", "")  #remeber to retrun
print_input(word) #$ Start
print(try_update_letter_guessed(word, old_letters))


print(old_letters)


#% Print letter > Print True if valid input type > Print True if valid input not in list > Print old letter List
# print(word[1:])





# * word_length = len(word)
# * print("_ " * word_length)

# first_try = input("Guess a letter: ").lower()
# print(first_try)

