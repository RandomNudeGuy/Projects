def is_greater(my_list, n):
    new_list = []
    for i in my_list:
        if i > n:
            new_list += [i]
        else:
            continue
    return new_list


result = is_greater([1, 30, 25, 60, 27, 28], 28)
print(result)

