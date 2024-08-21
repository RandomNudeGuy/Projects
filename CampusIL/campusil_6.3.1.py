list_1 = [0.6, 1, 2, 3]
list_2 = [3, 2, 0.6, 1]
list_3 = [9, 0, 5, 10.5]

def are_lists_equal(list1, list2):
    if sorted(list1) == sorted(list2):
        return True
    else:
        return False
    
print(are_lists_equal(list_1, list_2))
