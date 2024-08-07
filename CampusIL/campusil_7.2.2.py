def numbers_letters_count(my_str:str):
    num = 0
    letter = 0
    for i in my_str:
        if i.isdigit():
            num += 1
        else:
            letter += 1
    list1 = [num, letter]
    return list1


print(numbers_letters_count("Python 3.6.3"))
    

