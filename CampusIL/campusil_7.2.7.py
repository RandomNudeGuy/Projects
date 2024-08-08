def arrow(my_char, max_length):
    before_after = 0
    current = 0
    for i in range(0, max_length + 1):
        if before_after == 0 and current > 0:
            print(my_char * current)
            current += 1
            if current == max_length:
                print(my_char * current)
                current -= 1
                before_after += 1
        elif before_after == 1:
            for i in range(max_length, 0, -1):
                print(my_char * current)
                current -= 1
        elif current == 0:
            current += 1

arrow("!", 10)