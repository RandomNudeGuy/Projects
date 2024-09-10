
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

HANGMAN_PHOTOS = {"One": STAGE_ONE, "Two": STAGE_TWO, "Three": STAGE_THREE, "Four": STAGE_FOUR, "Five": STAGE_FIVE, "Six": STAGE_SIX, "Seven": STAGE_SEVEN}

old_letters = []
underlined_list = []
check_win_value = 0
already_guessed = []
num_of_triess = 0

def print_hangman(num_of_tries):
    global num_of_triess
    if num_of_triess == 1:
        print(HANGMAN_PHOTOS["One"])
    if num_of_triess == 2:
        print(HANGMAN_PHOTOS["Two"])
    if num_of_triess == 3:
        print(HANGMAN_PHOTOS["Three"])
    if num_of_triess == 4:
        print(HANGMAN_PHOTOS["Four"])
    if num_of_triess == 5:
        print(HANGMAN_PHOTOS["Five"])
    if num_of_triess == 6:
        print(HANGMAN_PHOTOS["Six"])
    if num_of_triess >= 7:
        print(HANGMAN_PHOTOS["Seven"])
        print("YOU LOST")
    else:
        return
    
def print_input(letter_guessed):   #% prints the letter guessed and first check for valid input
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
        print("False: Invalid Input")

def is_valid_input(letter_guessed): #% second check if valid input
    if word.isalpha() == False and word[1:] != "":
        print("False: Invalid Input")
    elif word.isalpha() == False:
        print("False: Invalid Input")
    elif word[1:] != "":
        print("False: Invalid Input")
    elif word[1:] == "":
        print("True: Valid Input")
        check_valid_input(word, old_letters)
    else:
        print("False: Invalid Input")

def check_valid_input(letter_guessed, old_letters_guessed): #% third check for valid input. checks if already guessed
    if letter_guessed not in old_letters_guessed:
        return True
    else:
        return False
 
def try_update_letter_guessed(letter_guessed, old_letters_guessed): #% adds letter guessed to already guessed, else shows what already guessed
    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        global old_letters
        old_letters += word
        return True
    else:
        new_list = " -> ".join(old_letters)
        print("X\n" + new_list)
        return False

def show_hidden_word(secret_word:list, old_letters_guessed): #%unvails the words 
    global underlined
    global word_length
    global word
    global indices
    global num_of_triess
    for i in secret_word:
        if indices != []:
            for a in indices:
                finder = int(a)
                if word in old_letters_guessed: #! already gueesed
                    # print(underlined)
                    messege = "Letter already guessed"
                elif (word not in old_letters_guessed) and (word in secret_word): #$ good guess
                    underlined[finder] = word
                    messege = "Good guess!"
        elif word not in secret_word: #% bad guess
            # print(*underlined)
            messege = "Try again"
        else: #! how??
            # print(*underlined)
            messege = "Else"
    if messege != "Good guess!":
        num_of_triess += 1
    print(*underlined)
    print(messege) 

def get_indices(element, string): #% finds positions of letter in a word
    indices = []
    for i in range(len(string)):
        if string[i] == element:
            indices.append(i)
        else:
            continue
    return indices #% find the positions of a letter in a word
    
def check_win(secret_word, old_letters_guessed:list): #% checks for win
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True
    
def choose_word(file_path, index:int):
    with open(file_path, "r") as file:
        file_path = file.read()
        stripper = file_path.strip()

    WordList = []
    splitter = stripper.split(" ")
    for i in splitter:
        if i not in WordList:
            WordList.append(i)
        else:
            continue
    len_splitter = len(splitter)
    len_WordList = len(WordList)
    if index > len_splitter:
        index_Extra = index % len_splitter
        print(index_Extra)
        index_WordList = splitter[index_Extra - 1]
        return len_WordList, index_WordList
    else:
        index_WordList = splitter[index - 1]
        return len_WordList, index_WordList

    


print(choose_word(r"/Users/mcrandom/Library/Mobile Documents/com~apple~CloudDocs/Python Projects/Projects/CampusIL/hangman_wordlist.txt", 3))

# word_toguess = [input("Enter a word to guess: ").lower()] #input word to guess 
# word_toguess_list = []
# for i in word_toguess[0]:
#     word_toguess_list.append(i) #! word >>> ['w', 'o', 'r', 'd']

# word_length = len(word_toguess[0])
# empty_space = "_ "
# underlined = []
# for i in range(word_length):
#     underlined.append(empty_space) 

# while True:
#     word = input("Please enter a letter: ").lower()
#     word = word.replace(" ", "")  #remeber to retrun
#     indices = get_indices(word, word_toguess_list)  #! position of letter
#     # print(indices)
#     print_input(word) #$ Start
#     # print(word_guess_underline(word_toguess))
#     show_hidden_word(word_toguess_list, old_letters)
#     try_update_letter_guessed(word, old_letters)
#     print(print_hangman(num_of_triess))
#     print(check_win(word_toguess[0], old_letters))

#     print(old_letters)
    


