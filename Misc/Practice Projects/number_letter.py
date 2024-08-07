
answer = input("Type your string: ")
# print(answer)


digit = 0 
letter = 0 

for i in answer:
    if i.isdigit():
        digit += 1

    elif i.isalpha():
        letter += 1

print(f"""Number of letters: {letter}
Number of digit {digit}""")