
#! DIFFERENT BUT SAME OUTPUT
#? DOES IT WORK THO?

first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
long_tuple = ()
def mult_tuple(tuple1, tuple2):
    for i in tuple1:
        for x in tuple2:
            tuple = ((i, x),)
            rev_tuple = ((x, i),)
            global long_tuple
            long_tuple += tuple 
            long_tuple += rev_tuple


    return long_tuple


print(mult_tuple(first_tuple, second_tuple))
