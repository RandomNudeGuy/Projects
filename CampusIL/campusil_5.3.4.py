def last_early(my_str):
    if my_str[-1] in my_str[:-1]:
        print(True)
    elif my_str[-1] not in my_str[:-1]:
        print(False)

word = input("Enter a string: ").lower()

last_early(word)