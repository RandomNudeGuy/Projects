first_tuple = (1, 2)
second_tuple = (4, 5)
long_tuple = ()
def mult_tuple(tuple1, tuple2):
    for i in tuple1:
        for x in tuple2:
            tuple = (i, x) 
            global long_tuple
            long_tuple += tuple


    return long_tuple


print(mult_tuple(first_tuple, second_tuple))
