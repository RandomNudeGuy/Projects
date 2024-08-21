
#% Goal: create a function that takes a list of 3 items (could be int, str, or whatever)
#% and moves the items one step to the left  (example: [1, 2, 3] > [2, 3, 1])

#$ First Option
def shift_left_op1(my_list):
    a, b, c = my_list
    new_list = [b, c, a]
    # print(new_list)
    return new_list

shift_left_op1(['monkey', 2.0, 1])

#$ Second Option
def shift_left_op2(my_list):
    a, b, c = my_list
    # print([b, c, a])
    return my_list

shift_left_op2(['monkey', 2.0, 1])

