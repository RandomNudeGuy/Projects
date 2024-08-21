word = input("Enter a word: ")
length = len (word)
length_halved = length // 2
new_word_lower = word[:length_halved].lower()
new_word_upper = word[length_halved:].upper()
print (new_word_lower + new_word_upper)