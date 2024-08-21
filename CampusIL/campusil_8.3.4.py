course_dict = {'I': 3, 'love': 3, 'self.py!': 2}

def inverse_dict(my_dict:dict):
    reversed_dict = {}
    first_list = []
    second_list = []
    for key, value in my_dict.items():
        if value == 3:
            first_list.append(key)
        if value == 2:
            second_list.append(key)
    for k, v in my_dict.items():
        if v == 3:
            reversed_dict[v] = first_list
        if v == 2:
            reversed_dict[v] = second_list
    # print(first_list, second_list)
    return reversed_dict




print(inverse_dict(course_dict))