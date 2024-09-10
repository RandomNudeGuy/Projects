import random
import time

for i in range(10):
    num = random.randrange(1, 6)
    print(num)
    time.sleep(2)


#% with open(r"/Users/mcrandom/Library/Mobile Documents/com~apple~CloudDocs/Python Projects/Projects/CampusIL/hangman_wordlist.txt", "r") as file:
# %        file_read = file.read()

# %stripper = file_read.strip()
# %splitter = stripper.split()

# %print(random.choices(splitter, k = 2p))