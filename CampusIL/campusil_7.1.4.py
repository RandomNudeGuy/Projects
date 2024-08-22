def squared_numbers(start:int, stop:int):
    # a = start
    # b = stop
    list1 = []
    while start <= stop:
        list1 += [start ** 2]
        start += 1
    print(list1)

squared_numbers(-3, 3)
squared_numbers(4, 8) 

