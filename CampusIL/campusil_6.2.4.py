y = [1, 2, 3]
x = [4, 5, 6]
nothing = ""
def extend_list_x(list_x, list_y):
    list_x = [*list_y, *list_x]
    return list_x

print(extend_list_x(x, y))

#$ Operator " * " is used in lists also to unpack them. eg: *list > 1, 2, 3| list > [1, 2, 3]