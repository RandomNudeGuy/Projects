course_dict = {'I': 3, 'love': 3, 'self.py!': 2}

def inverse_dict(my_dict:dict):
    reversed_dict = {}
    first_list = []
    second_list = []
    for key, value in my_dict.items():
        if value == 3:
            first_list.append(key)
            reversed_dict[value] = first_list
        if value == 2:
            second_list.append(key)
            reversed_dict[value] = second_list
    return reversed_dict




print(inverse_dict(course_dict))