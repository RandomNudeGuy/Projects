
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






old_letters = []
underlined_list = []
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

# def word_guess_underline(string:list):
#     word_length = len(string[0])
#     underlined = "_ " * word_length
#     print(string)
#     return underlined
    
def show_hidden_word(secret_word:list, old_letters_guessed):
    # word_length = len(secret_word[0])
    # empty_space = "_ "
    # underlined = []
    # for i in range(word_length):
    #     underlined.append(empty_space)
    global underlined
    global word
    print(underlined)
    for i in secret_word:
        finder = int(secret_word[0].find(word))
        print(finder)
        if word in old_letters_guessed: #! already gueesed
            print(underlined)
            messege = "Letter already guessed"
            return messege
        elif word not in old_letters_guessed and word in secret_word[0]: #$ good guess
            underlined[finder] = word
            print(underlined)
            messege = "Good guess!"
            continue
        elif word not in old_letters_guessed and word not in secret_word[0]: #% bad guess
            print(underlined)
            messege = "Try again"
            return messege
        else: #! how??
            print(underlined)
            messege = "Else"
            return messege


word_toguess = [input("Enter a word to guess: ")]

word_length = len(word_toguess[0])
empty_space = "_ "
underlined = []
for i in range(word_length):
    underlined.append(empty_space)

while True:
    word = input("Please enter a letter: ").lower()
    word = word.replace(" ", "")  #remeber to retrun
    print_input(word) #$ Start
    # print(word_guess_underline(word_toguess))
    print(show_hidden_word(word_toguess, old_letters))
    print(try_update_letter_guessed(word, old_letters))
    
    print(old_letters)




        
#% Print letter > Print True if valid input type > Print True if valid input not in list > Print old letter List
# print(word[1:])





# first_try = input("Guess a letter: ").lower()
# print(first_try)

