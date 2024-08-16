
#! DIFFERENT BUT SAME OUTPUT
#? DOES IT WORK THO?


# first_tuple = (1, 2)
# second_tuple = (4, 5)
#$((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))
#%((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))

# first_tuple = (1, 2, 3)
# second_tuple = (4, 5, 6)
#$((1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 1), (5, 1), (6, 1), (4, 2), (5, 2), (6, 2), (4, 3), (5, 3), (6, 3))
#%((1, 4), (4, 1), (1, 5), (5, 1), (1, 6), (6, 1), (2, 4), (4, 2), (2, 5), (5, 2), (2, 6), (6, 2), (3, 4), (4, 3), (3, 5), (5, 3), (3, 6), (6, 3))

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
