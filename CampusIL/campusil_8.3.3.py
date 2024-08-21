magic_str = "abra cadabra"

def count_chars(my_str:str):
    my_dict = {}
    for i in my_str:
        if i == " ":
            continue
        else:
            counter = my_str.count(i)
            if i not in my_dict:
                my_dict[i] = counter
            elif i in my_dict:
                continue

    return my_dict



print(count_chars(magic_str))