word = input("Enter a word: ")
first_letter = word[0]
# letters = word.find(first_letter)
temp_word = word.replace(first_letter, 'e')



print(first_letter + temp_word[1::])

